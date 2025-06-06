"""Dialog for initial NonMouse configuration."""

import tkinter as tk


def tk_arg() -> tuple[int, int, float, tuple[int, int]]:
    """Prompt the user for configuration values."""
    root = tk.Tk()
    root.title("First Setup")
    root.geometry("370x320")
    screenRes = (
        root.winfo_screenwidth(),
        root.winfo_screenheight(),
    )  # Get display resolution ディスプレイ解像度取得
    Val1 = tk.IntVar()
    Val2 = tk.IntVar()
    Val4 = tk.IntVar()
    Val4.set(30)  # Default mouse sensitivity デフォルトマウス感度
    place = ["Normal", "Above", "Behind"]
    # Camera #########################################################################
    tk.Label(text="Camera").grid(row=1)
    for i in range(4):
        tk.Radiobutton(root, value=i, variable=Val1, text=f"Device{i}").grid(
            row=2,
            column=i * 2,
        )
    tk.Label(text="     ").grid(row=3)
    # Place #########################################################################
    tk.Label(text="How to place").grid(row=4)
    for i in range(3):
        tk.Radiobutton(root, value=i, variable=Val2, text=f"{place[i]}").grid(
            row=5,
            column=i * 2,
        )
    tk.Label(text="     ").grid(row=6)
    # Sensitivity ###################################################################
    tk.Label(text="Sensitivity").grid(row=7)
    tk.Scale(root, orient="h", from_=1, to=100, variable=Val4).grid(row=8, column=2)
    tk.Label(text="     ").grid(row=9)
    tk.Button(text="continue", command=root.destroy).grid(row=10, column=2)
    # Wait 待機
    root.mainloop()
    # Output 出力
    cap_device = Val1.get()  # 0,1,2
    mode = Val2.get()  # 0:youself 1:
    kando = Val4.get() / 10  # 1~10
    return cap_device, mode, kando, screenRes
