# # # import os
# # # import cv2

# # # name = "lfpw"
# # # tag = "Preprocessed"
# # # resizedDir = "./data/" + name + tag + "/"    
# # # files = os.listdir(resizedDir)
# # # img = cv2.imread(resizedDir + files[4])

# # # print img.shape
# # # # print img

# # # # img = img * 255
# # # # cv2.imshow("img", img)
# # # # cv2.waitKey(0)

# # i = 15

# # while i > 2:
# # 	while i >5:
# # 		i -= 1
# # 		print "inside ", i
# # 		if i < 10:
# # 			break
# # 	raise "debug"
# # 	print "outside ", i
# # print i


# # a = "123234"

# # print a[-2:]

# import os

# trainTestDir = "./data/trainTestData/"
# print os.path.isfile(trainTestDir + "firstAEDoutput2016-11-24 15:40:19.353189.p")

a = "3262777136_1Normalized0.p"
b = "3262777136_1Landmarks0.p"

position = a.index("Normalized")
header = a[: position]
print header
ender = a[position + len("Normalized"):]
print ender
c = header + "Landmarks" + ender
print c
print c == b