from winreg import *
import os
import sys
import win32com.shell.shell as shell

# 관리자 권한 설정
if sys.argv[-1] != 'asadmin':
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)


# 레지스트리 key 생성
key_path = r"Directory\Background\shell\FS Change"
CreateKey(HKEY_CLASSES_ROOT, key_path)
key_path = r"Directory\Background\shell\FS Change\Command"
CreateKey(HKEY_CLASSES_ROOT, key_path)

# HKEY_CLASSES_ROOT와 연결 후 핸들 얻음
reg_handle = ConnectRegistry(None, HKEY_CLASSES_ROOT)

# 얻은 핸들을 사용해 WRITE 권한으로 레즈스트리 키를 엶
key = OpenKey(reg_handle, key_path, reserved=0, access=KEY_WRITE)
data = r'''powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\\Users\\youjh\\anaconda3\\shell\\condabin\\conda-hook.ps1' ; conda activate 'C:\\Users\\youjh\\anaconda3' "; conda deactivate ; conda activate yolov5_pytorch110; python C:\\Users\\youjh\\Documents\\Github\\FileManagementUtils\\change_folder_structure.py "%V"; exit
'''

try:
    SetValueEx(key, "", 0, REG_SZ, data)
except:
    print("Encountered problems writing into the Registry...")

CloseKey(key)


