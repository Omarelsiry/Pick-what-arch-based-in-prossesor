import os

def get_processor_arch():
    arch = os.popen('adb shell getprop ro.product.cpu.abi').read().strip()
    if 'arm64' in arch:
        return 'arm64-v8a'
    elif 'armeabi' in arch:
        return 'armeabi-v7a'
    elif 'x86_64' in arch:
        return 'x86_64'
    elif 'x86' in arch:
        return 'x86'
    else:
        return None

def display_options():
    print("Available processor architectures:")
    print("1. arm64-v8a")
    print("2. armeabi-v7a")
    print("3. x86_64")
    print("4. x86")

if __name__ == '__main__':
    arch = get_processor_arch()
    if arch is None:
        print("Unable to determine processor architecture.")
    else:
        print("Detected processor architecture:", arch)
        display_options()
