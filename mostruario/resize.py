from PIL import Image

def resize(original, base):
    largura, altura = original.size
    vsize = int(largura * base/altura)
    hsize = int(altura * base/largura)
    if altura > largura:
        original = original.resize((vsize, base), Image.Resampling.LANCZOS)
    else:
        original = original.resize((base, hsize), Image.Resampling.LANCZOS)
    return original