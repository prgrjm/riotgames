import pandas
import tensorflow
import keras

championid = pandas.read_csv('tf_championid2.csv')
win = pandas.read_csv('tf_win.csv')
print(championid.shape, win.shape)

model = keras.Sequential([
    keras.layers.Input(shape=[314]),
    keras.layers.Dense(55),
    keras.layers.Dense(10),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

model.fit(championid[:30000], win[:30000], epochs=30)

alpha, beta = model.evaluate(championid[30000:], win[30000:])
print(alpha, beta)

# 말하자면 총 45개의 관계선이 있는거지 거기에 자기 자신의 벨류까지 있는거임 합쳐서 45개의 관계선 + 자기자신선 10개 총 55개

#또한 한 칸단 158개의 원샷변수가 있겠지

#이렇게 나눈 후에, 계산으로 비슷한 유형의 챔피언들을 분류한다. 그리고 거기에서 다시 유형 챔피언의 팀의 vs승률을 계산한다.

# 신드라와 라이즈랑 잘맞고, 제드와 야스오랑은 잘 안맞는 유형의 챔피언들을 한곳에 분류한다.
