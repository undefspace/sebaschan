import aioesphomeapi, yaml, asyncio, random
from dns import resolver

secrets = yaml.unsafe_load(open("../secrets.yaml"))
password = secrets["api"]["password"]

async def main():
    loop = asyncio.get_event_loop()

    for i in ['/', '-', '\\', '|'] * 4:
        await asyncio.sleep(0.1)
        print(f"{i} GateHacker 1.2.44.2 engaging {i}", end="\r")
    print(flush=True)

    print("Identifying target...")
    rsv = resolver.Resolver()
    rsv.nameservers = ["10.98.0.1"]
    target = rsv.resolve("sebaschan.lan")
    host = target.rrset[0].address

    await asyncio.sleep(0.2)

    print("Spooling up connections...")
    client = aioesphomeapi.APIClient(loop, host, 6053, password)
    await client.connect(login=True)
    await asyncio.sleep(0.2)

    print("Hacking the gate...")
    await asyncio.sleep(0.2)

    switch: aioesphomeapi.BinarySensorInfo = filter(
        lambda s: s.object_id == 'open_ring_one_door',
        (await client.list_entities_services())[0]
    ).__next__()

    await client.switch_command(switch.key, 1)

    msg = "! GATE 0 HACK3D !"
    trg = list(" " * len(msg))
    src = list(enumerate(msg))
    random.shuffle(src)
    for i, k in src:
        trg[i] = k
        print(f"\r {''.join(trg)} ", end="", flush=True)
        await asyncio.sleep(0.04)
    await asyncio.sleep(0.2)

    print()
    input("Press enter to close the door...")
    await client.switch_command(switch.key, 0)

asyncio.run(main())
