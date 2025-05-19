import matplotlib.pyplot as plt
import pandas as pd
import os

def generate_graph_image():
    # สร้างกราฟสมมติ
    df = pd.DataFrame({
        "day": list(range(1, 11)),
        "price": [100, 102, 101, 105, 108, 107, 110, 115, 117, 120]
    })

    plt.figure()
    plt.plot(df["day"], df["price"], marker='o')
    plt.title("🔮 ตัวอย่างกราฟดัชนี")
    plt.xlabel("วัน")
    plt.ylabel("ราคา")
    image_path = "static/chart.png"
    os.makedirs("static", exist_ok=True)
    plt.savefig(image_path)
    plt.close()

    # สมมุติว่า Render โฮสต์ static ไฟล์ที่โดเมนนี้:
    return "https://<your-render-app>.onrender.com/static/chart.png"