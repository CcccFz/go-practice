FROM golang:1.12 AS build
RUN mkdir /src
COPY . /src
WORKDIR /src
RUN CGO_ENABLED=0 GOOS=linux go build -mod vendor -a -installsuffix cgo .

FROM alpine:latest
RUN apk add --no-cache ca-certificates && update-ca-certificates 2>/dev/null || true
RUN mkdir /app && mkdir /app/logs && mkdir /app/pem && mkdir /app/conf
WORKDIR /app
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
COPY --from=build /src/rental .
ENTRYPOINT ["/app/rental"]
