import pyautogui
from PIL import Image
from aip import AipOcr
import time

""" 你的 APPID AK SK """
APP_ID = '44160039'
API_KEY = '6d2zKTSOZ56fSMDdQjkPhasB'
SECRET_KEY = 'GXtl4RZzRL6paQBp9fUs96fGgnz2Qfmv'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
imagedir = "E:\MyLife\AI\classskip"
#读取文件
def get_file_content(filePath):
      with open(filePath, "rb") as fp:
         return fp.read()

#找到返回结果中的指定文字，并返回其位置
def find_word_location(result, target_word):
    for item in result['words_result']:
        if target_word in item['words']:
            return item['location']
    return None

#根据坐标字典{'top': 50, 'left': 11, 'width': 42, 'height': 30}，鼠标点击指定坐标
def click_location(location):
    x = location['left'] + location['width'] / 2
    y = location['top'] + location['height'] / 2
    pyautogui.click(x, y)

#定时截图并识别文字，并完成点击
def time_to_click():
    # 截取屏幕快照
    screenshot = pyautogui.screenshot()
      # 将图片转为灰度模式
    screenshot = screenshot.convert('L')
    # 保存截图到指定路径
    screenshot.save(r'E:\MyLife\AI\classskip\image.png')
    print("已截图并保存到：" + imagedir + "\image.png")

    #调用API丙返回参数
    myimage = get_file_content(imagedir + '\image.png')
    result = client.general(myimage)
    print(result)
 
    #找到指定字符
    pause_loc = {'top': 600, 'left': 1700, 'width': 2, 'height': 2}
    res_loc_1 = find_word_location(result, '确定')
    print('res_loc_1:',res_loc_1)
    if res_loc_1 != None:
        click_location(res_loc_1) #如果暂停，点击确定
        time.sleep(5) #加载时间
        click_location(pause_loc) #可能需要多点一次才能继续播放
    else:
        res_loc_2 = find_word_location(result, '下一节')
        print('res_loc_2:',res_loc_2)
        if res_loc_2 != None:
            click_location(res_loc_2) #点击下一节
            time.sleep(5) #加载时间
            click_location(pause_loc) #可能需要多点一次才能继续播放
        else:
            print("未找到查找内容")
            return None

def main():
    waiting_sec = 1800 #触发间隔时间
    while True:
        print("事件触发")
        time_to_click()
        time.sleep(waiting_sec)  #间隔时间后触发一次

main()
