from PIL import Image

marca = Image.open(('marca.png'))
base = 1000
largura, altura = marca.size
vsize = int(largura * base/altura)
lanc = marca.resize((vsize, base), Image.Resampling.LANCZOS)
lanc1 = marca.resize((vsize, base))
lanc.show()
lanc1.show()