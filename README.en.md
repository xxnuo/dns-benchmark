# dnspy - Test DNS Servers Worldwide

[English](./README.en.md) | [中文](./README.md)

**The English translation may lag behind the Chinese original. For current details, see the Chinese version.**

**The English translation may lag behind the Chinese original. For current details, see the Chinese version.**

**The English translation may lag behind the Chinese original. For current details, see the Chinese version.**

### Data Analysis Dashboard Preview

![Data Analysis Dashboard Preview](./images/preview.png)

[Data Analysis Dashboard with Sample Data](https://bench.dash.2020818.xyz)

## Testing Tool

Download the `dnspy-*` file according to your system architecture from the [releases](https://github.com/xxnuo/dns-benchmark/releases) page. For example, if you're using macOS with an Intel processor, download the `dnspy-darwin-amd64` file.

**You must disable all proxy software's Tun mode and virtual network card mode, otherwise it will affect the test results.**

Rename the file to `dnspy` (or `dnspy.exe` on Windows), open a terminal, navigate to the directory containing the file, and execute the following command to start testing:

```bash
unset http_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY ALL_PROXY
./dnspy
```

Follow the prompts to start the test.

By default, multi-threading mode is used to speed up testing. However, the default parameter of 10 threads requires at least 1 MB/s network bandwidth and a minimum of 4 CPU cores.
If your network or processor is not powerful enough, it will lead to inaccurate test results. You must use the `-w` parameter to reduce the number of threads.

After the test is complete, the results will be output to a JSON file in the current directory with a name like `dnspy_result_2024-11-07-17-32-13.json`.

Enter `Y` or `y` or just press Enter as prompted, and the data analysis dashboard website will automatically open. Click the `Read Analysis` button in the top right corner of the website, select your JSON file, and you can see the visualized test results.

## Compile the Testing Tool

Required environment for compilation:

- You need `Go` environment and `curl` command on your computer
- Ability to access Github to download resource files

Compilation process:

```bash
# Clone this repository
git clone https://github.com/xxnuo/dns-benchmark.git
cd dns-benchmark/dnspy
# Update required data (requires VPN)
make update
make
./dnspy
``` 