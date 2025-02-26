import requests
import os
import shutil
from google.colab import files

# List of URLs to download
urls = ['https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R06.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R06.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R06.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R06.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R06.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R05.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R04.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R03.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R02.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R01.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R01.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R01.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R01.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R01.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R01.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R01.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_R01.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H31.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H31.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H31.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H31.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H30.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H29.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.9.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.8.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.7.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.6.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.5.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.4.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.3.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.2.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H28.1.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H27.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H26.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H25.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H24.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H23.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H22.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H21.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H20.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.04.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.03.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.02.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H19.01.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.12.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.11.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.10.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.09.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.08.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.07.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.06.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.05.xls',
'https://www.mlit.go.jp/toukeijouhou/chojou/ex/labor_xls_data/labor_H18.04.xls'
]

# Designated local directory to save files (Colab uses '/content/')
local_directory = '/content/downloads'

# Ensure the directory exists
os.makedirs(local_directory, exist_ok=True)

# Download each file
for url in urls:
    response = requests.get(url)
    filename = url.split('/')[-1]
    file_path = os.path.join(local_directory, filename)

    with open(file_path, 'wb') as f:
        f.write(response.content)

# Create a ZIP archive of the downloads folder
shutil.make_archive('/content/downloads', 'zip', '/content/downloads')

# Download the ZIP file to your local machine
files.download('/content/downloads.zip')

print("Download completed! The files have been zipped and are ready for download.")
