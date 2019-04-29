package com.pris.test;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.robotium.solo.Solo;

import android.app.Instrumentation;
import android.content.Intent;
import android.test.ActivityInstrumentationTestCase2;
import android.view.View;
import android.widget.Button;
import junit.framework.Assert;
import other.R;

@SuppressWarnings("rawtypes")
public class FirstTestCase extends ActivityInstrumentationTestCase2 {

    private static final String TARGET_PACKAGE_ID = "com.netease.pris";
    private static final String LAUNCHER_ACTIVITY_FULL_CLASSNAME = "com.netease.pris.activity.MainGridActivity";
    private static Class launcherActivityClass;
    
    private Solo solo;
    static {
        try {
            launcherActivityClass = Class.forName(LAUNCHER_ACTIVITY_FULL_CLASSNAME);
            } catch (ClassNotFoundException e){
              throw new RuntimeException(e);
            }
       }
    
    @SuppressWarnings({ "unchecked", "deprecation" })
    public FirstTestCase(){
        super(TARGET_PACKAGE_ID,launcherActivityClass);
    }
    
    @Before 
    protected void setUp() throws Exception {
        super.setUp();
        /*��һ�׳�ʼ�����������������������MainActivity�������ֻҪ����һ�д���Ϳ���
          this.solo = new Solo(getInstrumentation(), getActivity());*/
        //�ڶ��׳�ʼ�������������������治��MainActivity�������ʹ��Intent��Ӧ�ó���������
        Instrumentation instrumentation = getInstrumentation();
        this.solo = new Solo(instrumentation); 
        final String targetPackage = instrumentation.getTargetContext()
                .getPackageName();

        Intent intent = new Intent(Intent.ACTION_MAIN);
        intent.setClassName(targetPackage,
                "com.netease.pris.activity.MainGridActivity");
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        instrumentation.getTargetContext().startActivity(intent);   
    }

    @Test
    public void testLogin() {
        boolean isOk = solo.waitForActivity("com.netease.pris.activity.MainGridActivity", 5000);
        Assert.assertTrue("û�е���Ӧ��", isOk);
        solo.sleep(3000);
        //���������˺�ҳ��
        boolean isFindAccountButton = solo.waitForView(R.id.account_btn, 1, 2000);
        Assert.assertTrue("û���ҵ��˺ſؼ�", isFindAccountButton);
        View account_button = solo.getView(R.id.account_btn);
        solo.clickOnView(account_button);
       //�����½��ť���򿪵�½ҳ��
        boolean isLoginButton = solo.waitForView(R.id.button_login, 1, 2000);
        Assert.assertTrue("û���ҵ���½�ؼ�", isLoginButton);
    }

    @After
    public void tearDown() throws Exception {
        solo.finishOpenedActivities();
    }
}