import requests
version="1.7.103.0"
resp1=requests.get(f"https://api.github.com/repos/ClassIsland/ClassIsland/releases/tags/{version}",verify=False);
release_id=resp1.json()["id"]
resp2=requests.get(f"https://api.github.com/repos/ClassIsland/ClassIsland/releases/{release_id}/assets",verify=False);
files=resp2.json()

for arch in ["x64","arm64"]:
    filename=f"ClassIsland_app_linux_{arch}_selfContained_deb.deb"
    file=[f for f in files if f["name"]==filename][0]
    size=file["size"]
    sha256=file["digest"].replace("sha256:","")
    created=file["created_at"]
    print(f"arch: {arch}, size: {size}, sha256: {sha256}, created: {created}")