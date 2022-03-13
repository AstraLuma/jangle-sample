from jangle import schedule


@schedule.every(1).minute.do
def check_in_sync():
    print("Checking in, synchronously!")


@schedule.every(1).minute.do
async def check_in_async():
    print("Checking in, asynchronously!")
