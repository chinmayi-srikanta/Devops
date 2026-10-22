import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    detach=True,
    security_opt=["apparmor=my-apparmor-profile"]
)

result1 = container.exec_run("cat /etc/passwd")
print("Read /etc/passwd:", result1.exit_code)
print(result1.output.decode())

result2 = container.exec_run("/bin/bash")
print("Execute bash:", result2.exit_code)
print(result2.output.decode())

container.stop()
container.remove()