
# Plot trajectory of gradient colors and overlay on the overlaid figure

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image

# Load CSV file, path and file name
data = pd.read_csv('/PATH OF TRAKING DATA/TRACKING DATA.csv')

# Load background image, path and file name
background_image = Image.open('/PATH OF MICROMOTOR MOTION IMAGE/MICROMOTOR IMAGE.jpg')

# Calculate pixel size per micron
pixel_size = 3.6364

from matplotlib import cm
# Set colors for time frames
data['color'] = data['FRAME'] / data['FRAME'].max()

data['POSITION_Y'] = background_image.height / pixel_size - data['POSITION_Y']

# Plot trajectory
plt.figure(figsize=(10,8))
plt.imshow(background_image, extent=[0, background_image.width/pixel_size, 0, background_image.height/pixel_size])
scatter= plt.scatter(data['POSITION_X'], data['POSITION_Y'], c=data['color'], s=5, cmap='jet')
#colorbar = plt.colorbar(scatter)
colorbar = plt.colorbar(label='TIME', shrink=0.5,ticks=[0, 1])
colorbar.ax.tick_params(labelsize=12)  # Adjust color bar font size
colorbar.set_ticklabels(['T$_i$', 'T$_f$'])  # Set tick labels
plt.xlabel('X (µm)', fontsize=14,fontname='Times New Roman')  # Adjust x-axis label font size
plt.ylabel('Y (µm)', fontsize=14,fontname='Times New Roman')  # Adjust y-axis label font size
plt.title('RBC achiral micromotor localized delivery-rolling',fontsize=14,fontname='Times New Roman')
plt.xlim(0, background_image.width/pixel_size)
plt.ylim(background_image.height/pixel_size, 0)  # Invert y-axis limits
plt.gca().invert_yaxis()  # Invert y-axis to match image 
#plt.savefig('/PATH OF OUTPUT/OUTPUT IMAGE.jpg', dpi=300)  # Export figure as JPEG with high quality
plt.show()
