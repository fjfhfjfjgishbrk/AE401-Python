import tensorflow
from tensorflow import keras
from tensorflow.keras import layers


model = keras.Sequential()
model.add(keras.Input(shape=(7, 7, 3)))  # 250x250 RGB images
model.add(layers.Conv2D(40, 5, activation="relu", use_bias=True))
model.add(layers.Conv2D(40, 5, padding="same", activation="relu", use_bias=True))
model.add(layers.Conv2D(40, 5, padding="same", activation="relu", use_bias=True))
#model.add(layers.MaxPooling2D(pool_size=(2, 2)), padding="same")

# Can you guess what the current output shape is at this point? Probably not.
# Let's just print it:
model.summary()

# The answer was: (40, 40, 32), so we can keep downsampling...

# And now?
model.summary()

# Now that we have 4x4 feature maps, time to apply global max pooling.
#model.add(layers.GlobalMaxPooling2D())

# Finally, we add a classification layer.
#model.add(layers.Dense(10))