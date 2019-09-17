# Write It写入文本
# Demonstrates writing to a text file

print("Creating a text file with the write() method.")
text_file = open("write_it.txt", "w")
text_file.write("这是第一 行\n")
text_file.write("这是我写的第二行\n")
text_file.write("这是我用电脑写的第二行\n")
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()

print("\nCreating a text file with the writelines() method.")
text_file = open("write_it.txt", "w")
lines = ["这是第一 行\n",
         "这是我写的第二行\n",
         "这是我用电脑写的第二行\n"]
text_file.writelines(lines)
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()

input("\n\nPress the enter key to exit.")
