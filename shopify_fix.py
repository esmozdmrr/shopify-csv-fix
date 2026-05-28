import pandas as pd
import re

# Excel dosyasını oku
df = pd.read_excel("347984505-212208 (1).xlsx")

def duzenle(text):
    if pd.isna(text):
        return ""

    text = str(text)

    text = text.replace("KULLANIM ALANLARI", "\n\nKULLANIM ALANLARI\n")
    text = text.replace("ÜRÜN SAKLAMA & DEPOLAMA KOŞULLARI", "\n\nSAKLAMA VE DEPOLAMA KOŞULLARI\n")

    # Madde işaretleri
    text = re.sub(r"\s*•\s*", "\n• ", text)

    return text.strip()

# açıklamaları düzenle
df["Açıklama"] = df["Açıklama"].apply(duzenle)
df["Editör Yorumu"] = df["Editör Yorumu"].apply(duzenle)

# csv olarak kaydet
df.to_csv("shopify_duzenli.csv", index=False, encoding="utf-8-sig")

print("Hazır: shopify_duzenli.csv")
