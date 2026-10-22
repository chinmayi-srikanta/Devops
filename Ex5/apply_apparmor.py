import docker

client = docker.from_env()

image, build_logs = client.images.build(
    path=".",
    tag="flask-apparmor"
)

container = client.containers.run(
    "flask-apparmor",
    detach=True,
    ports={"5000/tcp": 5000},
    security_opt=["apparmor=my-apparmor-profile"]
)

container.reload()
print("Security options:", container.attrs["HostConfig"]["SecurityOpt"])

container.stop()
container.remove()