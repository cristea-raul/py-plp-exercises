from apis import Logger, ConfigReader


def main():
    Logger.setup('io_tests/oop-ex4-log')
    reader = ConfigReader()
    reader.read_config('io_tests/oop-ex2-config')
    print(reader)

    assert reader.contains('path')
    assert not reader.contains('somekey')

    assert reader.get_val('intval') == 10
    assert reader.get_val('floatval') == 0.332


if __name__ == "__main__":
    main()
