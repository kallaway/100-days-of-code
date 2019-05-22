import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

raw_data = pd.read_csv('ASEAN.csv')

countries = raw_data.iloc[:, 0]
imports = raw_data.iloc[:, 1]
exports = raw_data.iloc[:, 2]


n = np.arange(len(raw_data))

plt.figure("Domestic Import/Export ASEAN 2017")
plt.title("ASEAN Domestic Import/Export 2017")
import_export = plt.bar(x = n, height = imports, color = 'fuchsia', width = .40)
export_import = plt.bar(x = n, height = exports, color = 'mediumspringgreen', width = .40, bottom = imports)
plt.ylabel("Billions of USD")
plt.xticks(n, countries, rotation = 45)
plt.legend([import_export, export_import], ('Imports', 'Exports'))
plt.show()
