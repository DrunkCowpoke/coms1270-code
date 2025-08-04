# Trevor Bentley        7-16-2025
# Lab 7: Min Max sorter

# This droid evaluates a list of input int, and then finds min and max

# ----- Input Sector -----
def scoopUserJunk():
    memoryBank = []
    while True:
        payload = input("Enter a number (* to stop): ")
        if payload == "*":
            break
        memoryBank.append(payload)
    return memoryBank


# ----- min-----
def scanForWeakest(signalArray):
    weakest = signalArray[0]
    for signal in signalArray:
        if signal < weakest:
            weakest = signal
    return weakest
# ----- MAX -----
def scanForBeastMode(signalArray):
    strongest = signalArray[0]
    for signal in signalArray:
        if signal > strongest:
            strongest = signal
    return strongest
# ----- Going manual Main FXN -----
def main():
    rawTelemetry = scoopUserJunk()

    print("Rewiring input...")
    cleanTelemetry = []
    for chunk in rawTelemetry:
        cleanTelemetry.append(int(chunk))

    weakestSignal = scanForWeakest(cleanTelemetry)
    strongestSignal = scanForBeastMode(cleanTelemetry)

    print("System analysis complete.")
    print(" Weakest Signal:", weakestSignal)
    print(" Strongest Signal:", strongestSignal)

if __name__ == "__main__":
    main()