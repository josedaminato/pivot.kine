from pathlib import Path
from PIL import Image

base = Path(
    r"C:\Users\damin\.cursor\projects\c-Users-damin-OneDrive-Desktop-pivot-kine\assets"
)
out = Path(__file__).resolve().parents[1] / "assets" / "team"
out.mkdir(parents=True, exist_ok=True)

sources = {
    "lucas-felix": base
    / "c__Users_damin_AppData_Roaming_Cursor_User_workspaceStorage_0572a2225b0937e4785c21b03c2746fc_images_lucas-91a48054-3518-4830-9265-33b3bbb9d67e.jpg",
    "matias-frola": base
    / "c__Users_damin_AppData_Roaming_Cursor_User_workspaceStorage_0572a2225b0937e4785c21b03c2746fc_images_matias-3aaac0ce-f61d-4760-80bf-a21ee71e71c8.jpg",
    "guadalupe-oieni": base
    / "c__Users_damin_AppData_Roaming_Cursor_User_workspaceStorage_0572a2225b0937e4785c21b03c2746fc_images_guadalupe-d0dd1485-b307-4da3-87e1-5b70b26bd45b.jpg",
}

SIZE = 256


def crop_avatar(im: Image.Image) -> Image.Image:
    w, h = im.size
    side = min(w, h)
    left = (w - side) // 2
    top = int((h - side) * 0.12)
    top = max(0, min(top, h - side))
    cropped = im.crop((left, top, left + side, top + side))
    return cropped.resize((SIZE, SIZE), Image.Resampling.LANCZOS)


for name, src in sources.items():
    im = Image.open(src).convert("RGB")
    avatar = crop_avatar(im)
    jpg_path = out / f"{name}.jpg"
    webp_path = out / f"{name}.webp"
    avatar.save(jpg_path, "JPEG", quality=82, optimize=True, progressive=True)
    avatar.save(webp_path, "WEBP", quality=82, method=6)
    print(
        f"{name}: src {src.stat().st_size} B -> jpg {jpg_path.stat().st_size} B, "
        f"webp {webp_path.stat().st_size} B ({im.size[0]}x{im.size[1]} -> {SIZE}x{SIZE})"
    )

for old in out.glob("*.jpeg"):
    old.unlink()
    print("removed", old.name)
