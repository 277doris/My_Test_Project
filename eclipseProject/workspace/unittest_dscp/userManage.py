
# '''
#  Created on 2019��1��21��
#  
#  @author: ������
# '''
# *-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
#����������
from selenium.webdriver.support.select import Select

class users_manage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://dscp.super.com/#/")
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #��¼��������Ա     admin   111111
        #�����˺�
        username = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input")
        username.send_keys("admin")
        pw = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/input")
        pw.send_keys("111111")
        #������֤��
        check_code = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/input")
        check_code.send_keys("dscp")
        #�����¼����
        login = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[4]/div/button")
        login.click()
        time.sleep(3)
        
        #����û�����
        user_control = element('//*[@id="app"]/div/div[1]/div[2]/ul/li[3]')
        user_control.click()
        time.sleep(1)
        #����½��û�
        add_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div/button')
        add_user.click()
        time.sleep(1)
        #�½��û���������רԱ
        new_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        new_user.send_keys("cuishouZY")
        #�½��û���������
        new_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        new_name.send_keys('�Զ���Ӵ���')  
        #�½��û������ֻ���
        new_tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        new_tel.send_keys("13313331333")
        #�½��û���������
        new_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        new_pw.send_keys("111111")
        #�½��û�����ȷ������
        comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        comfirm_pw.send_keys('111111')
        #�½��û�����ѡ���λ
        position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #�½��û�����ѡ���λ
        Select(position).select_by_visible_text("ί�����")
        #�½��û�����ѡ���Ʒ
        checkbox1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[1]/span[1]/span')
        checkbox1.click()
        checkbox2 =element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[2]/span[1]/span')
        checkbox2.click()
        checkbox3 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[3]/span[1]/span')
        checkbox3.click()
        time.sleep(1)
        #���������ť
        create_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        create_button.click()
        time.sleep(1)
        # ��ȡalert�Ի���
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # ��ӡ����Ի�������
        print(dig_alert.text)
        # alert�Ի������ھ���Ի�����������ֻ�ܽ��ܵ���
        dig_alert.accept()
        time.sleep(3)
        print('�û��������½�ί����ճɹ�')
        
        #�༭��һ���˺�
        edit_first = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[6]/span/span[1]')
        edit_first.click()
        time.sleep(1)
        #�༭�ֻ���
        edit_phone = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        edit_phone.clear()
        edit_phone.send_keys('13313333333')
        #�༭����
        edit_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        edit_pw.clear()
        edit_pw.send_keys('111111')
        #�༭����ȷ������
        edit_comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        edit_comfirm_pw.clear()
        edit_comfirm_pw.send_keys('111111')
        #�༭��λ
        edit_position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #�༭��λΪ����רԱ
        Select(edit_position).select_by_visible_text("����רԱ")
        #ѡ��ֱ���쵼
        immediate_boss = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/select')
        time.sleep(1)
        #ѡ��ֱ���쵼Ϊ������Ʒ����
        Select(immediate_boss).select_by_visible_text("һ����Ʒ����")
        time.sleep(2)
        #����޸İ�ť
        edit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        edit_button.click()
        time.sleep(1)
        # ��ȡalert�Ի���
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # ��ӡ����Ի�������
        print(dig_alert.text)
        # alert�Ի������ھ���Ի�����������ֻ�ܽ��ܵ���
        dig_alert.accept()
        time.sleep(3)
        print('�û��������༭�˺ųɹ�')
        
        #ɾ���˺š���aaa
        delect_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[5]/td[6]/span/span[2]')
        delect_user.click()
        time.sleep(5)
        print('�û�������ɾ���˺ųɹ�')
        
        #�½��û�������������
        new_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        new_user.send_keys("daihouZG")
        #�½��û���������
        new_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        new_name.send_keys("�����Զ���Ӵ�������")       
        #�½��û������ֻ���
        new_tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        new_tel.send_keys("13313331333")
        #�½��û���������
        new_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        new_pw.send_keys("111111")
        #�½��û�����ȷ������
        comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        comfirm_pw.send_keys('111111')
        #�½��û�����ѡ���λ
        position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #�½��û�����ѡ���λ
        Select(position).select_by_visible_text("��������")
        #�½��û�����ѡ���Ʒ
        checkbox1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[1]/span[1]/span')
        checkbox1.click()
        checkbox2 =element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[2]/span[1]/span')
        checkbox2.click()
        checkbox3 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[3]/span[1]/span')
        checkbox3.click()
        time.sleep(1)
        #���������ť
        create_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        create_button.click()
        time.sleep(1)
        # ��ȡalert�Ի���
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # ��ӡ����Ի�������
        print(dig_alert.text)
        # alert�Ի������ھ���Ի�����������ֻ�ܽ��ܵ���
        dig_alert.accept()
        time.sleep(3)
        print('�û��������½��������ܳɹ�')
        
        #�½��û���������רԱ
        new_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        new_user.send_keys("daihouZY")
        #�½��û���������
        new_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        new_name.send_keys("�����Զ���Ӵ���רԱ")    
        #�½��û������ֻ���
        new_tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        new_tel.send_keys("13313331333")
        #�½��û���������
        new_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        new_pw.send_keys("111111")
        #�½��û�����ȷ������
        comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        comfirm_pw.send_keys('111111')
        #�½��û�����ѡ���λ
        position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #�½��û�����ѡ���λ
        Select(position).select_by_visible_text("����רԱ")
        #ѡ��ֱ���쵼
        immediate_boss = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/select')
        Select(immediate_boss).select_by_visible_text("������Ʒ����")
        time.sleep(1)
        #���������ť
        create_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        create_button.click()
        time.sleep(1)
        # ��ȡalert�Ի���
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # ��ӡ����Ի�������
        print(dig_alert.text)
        # alert�Ի������ھ���Ի�����������ֻ�ܽ��ܵ���
        dig_alert.accept()
        time.sleep(3)
        print('�û��������½�����רԱ�ɹ�')
        
        #�½��û���������ͷ�
        new_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        new_user.send_keys("daihouKF")
        #�½��û���������
        new_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        new_name.send_keys("�����Զ���Ӵ���ͷ�")   
        #�½��û������ֻ���
        new_tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        new_tel.send_keys("13313331333")
        #�½��û���������
        new_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        new_pw.send_keys("111111")
        #�½��û�����ȷ������
        comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        comfirm_pw.send_keys('111111')
        #�½��û�����ѡ���λ
        position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #�½��û�����ѡ���λ
        Select(position).select_by_visible_text("����ͷ�")
        #ѡ��ֱ���쵼
        immediate_boss = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/select')
        Select(immediate_boss).select_by_visible_text("������Ʒ����")
        time.sleep(1)
        #���������ť
        create_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        create_button.click()
        time.sleep(1)
        # ��ȡalert�Ի���
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # ��ӡ����Ի�������
        print(dig_alert.text)
        # alert�Ի������ھ���Ի�����������ֻ�ܽ��ܵ���
        dig_alert.accept()
        time.sleep(3)
        print('�û��������½�����ͷ��ɹ�')
    
    def test_tearDown(self):
        #�˳������
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()