import asyncio
from rich.console import Console
import dns.resolver

console = Console()

async def check_dns_record_with_resolver_async(domain, record_type, resolver_ip='8.8.8.8'):
    try:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [resolver_ip]
        return resolver.resolve(domain, record_type)[0].to_text()
    except Exception as e:
        console.print(f"[bold red]Exception during DNS resolution:[/bold red] {e}")
        return None

async def monitor_dns_changes_async(domain, record_type, interval):
    initial_record = await check_dns_record_with_resolver_async(domain, record_type)
    console.print(f"Initial DNS record: [bold blue]{initial_record}[/bold blue]")

    last_record = initial_record
    while True:
        current_record = await check_dns_record_with_resolver_async(domain, record_type)
        if current_record != last_record:
            console.print(f"[bold green]DNS record changed from[/bold green] {last_record} [bold green]to[/bold green] {current_record}")
            last_record = current_record
        await asyncio.sleep(interval)

if __name__ == '__main__':
    domain = input("Enter the domain to monitor: ")
    record_type = input("Enter the record type (e.g., A, MX): ")
    interval = int(input("Enter the monitoring interval (in seconds): "))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(monitor_dns_changes_async(domain, record_type, interval))
