import os
import multiprocessing


def read_msg(q, original_folder_name, new_folder_name, filename):
    f_read = open(os.path.join(original_folder_name, filename), 'rb')
    contend = f_read.read()
    f_read.close()
    
    f_write = open(os.path.join(new_folder_name, filename), 'wb')
    f_write.write(contend)
    f_write.close()
    
    print('{} copy end'.format(filename))
    q.put(filename)


def main():
    # input coping folder name
    original_folder_name = input('please input orignial folder name: ')
    # input new folder
    try:
        new_folder_name = 'new' + original_folder_name
        os.mkdir(new_folder_name)
    except Exception :
        pass
    # get all files name in folder
    filenames = os.listdir(original_folder_name)
    # create pool
    po = multiprocessing.Pool(5)
    # create queue for msg communication
    q = multiprocessing.Manager().Queue()
    # read and write file
    for filename in filenames:
        po.apply_async(read_msg, (q, original_folder_name, new_folder_name, filename,))
    # close pool
    po.close()
    # waiting for son process end
    # po.join()
    file_num = 0
    all_files_num = len(filenames)
    while True:
        file_name = q.get()
        file_num +=1
        print('{} copy end.'.format(file_name))
        print('The pecentage of copy files is: {:.2f}'.format(file_num/all_files_num))
        if file_num >= all_files_num:
            break
    



if __name__ == '__main__':
    main()
