# 默认目标
all: run

# 构建目标
build: 
	@echo "正在构建..."
	go mod tidy
	GOOS=darwin GOARCH=amd64 go build -ldflags "-s -w" -tags release -o dnspy-darwin-amd64 .
	GOOS=darwin GOARCH=arm64 go build -ldflags "-s -w" -tags release -o dnspy-darwin-arm64 .
	GOOS=linux GOARCH=amd64 go build -ldflags "-s -w" -tags release -o dnspy-linux-amd64 .
	GOOS=linux GOARCH=arm64 go build -ldflags "-s -w" -tags release -o dnspy-linux-arm64 .
	GOOS=windows GOARCH=amd64 go build -ldflags "-s -w" -tags release -o dnspy-windows-amd64.exe .
	GOOS=windows GOARCH=arm64 go build -ldflags "-s -w" -tags release -o dnspy-windows-arm64.exe .

# 运行目标
run:
	@echo "正在运行..."
	go run .

# 更新地理数据
update-geodata:
	@echo "正在更新地理数据..."
	curl https://cdn.jsdelivr.net/gh/Loyalsoldier/geoip@release/Country.mmdb -o ./res/Country.mmdb

# 更新域名数据
update-domains:
	@echo "正在更新域名数据..."
	curl https://cdn.jsdelivr.net/gh/Tantalor93/dnspyre@master/data/10000-domains -o ./res/domains.txt

# 更新 dnspyre 可执行文件
configuration:
	@echo "正在更新 dnspyre 可执行文件..."
	@echo "请勿修改使用的 dnspyre 版本号,否则会导致 dnspy 无法正常运行"
	go get github.com/tantalor93/dnspyre/v3@latest
	GOOS=darwin GOARCH=amd64 go build -ldflags "-s -w" -o ./res/dnspyre-darwin-amd64 github.com/tantalor93/dnspyre/v3
	GOOS=darwin GOARCH=arm64 go build -ldflags "-s -w" -o ./res/dnspyre-darwin-arm64 github.com/tantalor93/dnspyre/v3
	GOOS=linux GOARCH=amd64 go build -ldflags "-s -w" -o ./res/dnspyre-linux-amd64 github.com/tantalor93/dnspyre/v3
	GOOS=linux GOARCH=arm64 go build -ldflags "-s -w" -o ./res/dnspyre-linux-arm64 github.com/tantalor93/dnspyre/v3
	GOOS=windows GOARCH=amd64 go build -ldflags "-s -w" -o ./res/dnspyre-windows-amd64.exe github.com/tantalor93/dnspyre/v3
	GOOS=windows GOARCH=arm64 go build -ldflags "-s -w" -o ./res/dnspyre-windows-arm64.exe github.com/tantalor93/dnspyre/v3


update: update-geodata update-domains

.PHONY: all build run clean update-geodata update-caller update-domains
