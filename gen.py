import os
import random

mazeSrc = os.listdir('mazes')
mazeDest = os.listdir('gen_mazes')

pairs = {}
for mazeName in mazeSrc:
	my_file = open('mazes\\'+mazeName, "r")
	content_list = my_file.readlines()
	col_length = len(content_list[0])-1
	row_length = len(content_list)
	new_content = []

	for row in content_list:
		row = row.replace('P',' ')
		row = row.replace('.',' ')
		new_content.append(row)

	new_maze = new_content.copy()
	


	for number in range(5000):
		print(number)
		# seed = random.randint(0, 1000000000)
		new_content = new_maze.copy()
		insert_Px = random.randint(0, row_length-1)
		insert_Py = random.randint(0, col_length-1)
	
		px = row_length - insert_Px - 1

		while(new_content[px][insert_Py] =='%'):
			insert_Px = random.randint(0, row_length-1)
			insert_Py = random.randint(0, col_length-1)
			px = row_length - insert_Px - 1

	
		new_content[px] = new_content[px][0:insert_Py] + 'P' + new_content[px][insert_Py+1: ]

		insert_Gx = random.randint(0, row_length-1)
		insert_Gy = random.randint(0, col_length-1)
		gx = row_length - insert_Gx - 1

	
		while(new_content[gx][insert_Gy] =='%' or new_content[gx][insert_Gy] =='P'):
			insert_Gx = random.randint(0, row_length-1)
			insert_Gy = random.randint(0, col_length-1)
			gx = row_length - insert_Gx - 1
	
		new_content[gx] = new_content[gx][0:insert_Gy] + '.' + new_content[gx][insert_Gy+1: ]	

		# for i in content_list:
		# 	print(i)
	
		# for i in new_content:
		# 	print(i)
		print(px, insert_Py, gx, insert_Gy)

		print('_'*100)
		t1 = (px, insert_Py)
		t2 = (gx, insert_Gy)
		t3 = (t1, t2)
		
		if t3 in pairs:
			pairs[t3]+= 1
		else: 
			pairs[t3]= 1

		outfile = open('gen_mazes\\' + str(insert_Gx) + '_' + str(insert_Gy) + '_' + str(insert_Px) + '_' + str(insert_Py) + '_'  + mazeName , "w")
	
		for element in new_content:
			outfile.write(element)
		
		outfile.close()

