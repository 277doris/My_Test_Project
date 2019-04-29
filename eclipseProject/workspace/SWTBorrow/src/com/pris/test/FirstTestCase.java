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
        /*第一套初始化方法，适用于主界面就是MainActivity的情况，只要下面一行代码就可以
          this.solo = new Solo(getInstrumentation(), getActivity());*/
        //第二套初始化方法，适用于主界面不是MainActivity的情况，使用Intent打开应用程序主界面
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
        Assert.assertTrue("没有调起应用", isOk);
        solo.sleep(3000);
        //进入左栏账号页面
        boolean isFindAccountButton = solo.waitForView(R.id.account_btn, 1, 2000);
        Assert.assertTrue("没有找到账号控件", isFindAccountButton);
        View account_button = solo.getView(R.id.account_btn);
        solo.clickOnView(account_button);
       //点击登陆按钮，打开登陆页面
        boolean isLoginButton = solo.waitForView(R.id.button_login, 1, 2000);
        Assert.assertTrue("没有找到登陆控件", isLoginButton);
    }

    @After
    public void tearDown() throws Exception {
        solo.finishOpenedActivities();
    }
}