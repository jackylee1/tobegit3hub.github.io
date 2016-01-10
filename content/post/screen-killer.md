+++
date = "2016-01-10T08:35:27+08:00"
draft = true
title = "screen killer"

+++



## 简介

很早以前学C++的Win32编程，了解了一下创建窗口的知识，就想写个屏幕保护程序什么的。。。

## 成品

结果是写成了这个Screen Killer：就是以屏幕大小画矩形（也就是传说中的全屏了），其中用随机函数生成不同的颜色，每100ms更新一次。效果自己想像吧。

![](/images/screen_killer.jpg)

## 源代码

<pre><code>

//WinMain.cpp

#include<Windows.h>
#include<ctime> //to get a random seed
#include<stdlib.h> //to set the random color of screen

#define ID_TIMER 101

LRESULT CALLBACK WindowProc(
 __in HWND hWnd,
 __in UINT uMsg,
 __in WPARAM wParam,
 __in LPARAM lParam
);
int APIENTRY WinMain( HINSTANCE hInstance,
 HINSTANCE hPrevInstance,
 LPSTR lpCmdLine,
 int nCmdShow)
{
 srand( time(0) );

LPCWSTR lpClassName = TEXT("tobeScreenKiller");
 LPCWSTR lpWindowName = TEXT("Screen Killer");

WNDCLASS wc;
 wc.cbClsExtra = 0;
 wc.cbWndExtra = 0;
 wc.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
 wc.hCursor = LoadCursor(NULL, IDI_QUESTION);
 wc.hIcon = LoadIcon(NULL, IDI_SHIELD);
 wc.hInstance = hInstance;
 wc.lpfnWndProc = WindowProc;
 wc.lpszClassName = lpClassName;
 wc.lpszMenuName = NULL;
 wc.style = CS_HREDRAW | CS_VREDRAW;

RegisterClass(&wc);

HWND hWnd;
 hWnd = CreateWindow(lpClassName, lpClassName,
 WS_POPUP,
 CW_USEDEFAULT, CW_USEDEFAULT,
 CW_USEDEFAULT, CW_USEDEFAULT,
 NULL,
 NULL,
 hInstance,
 NULL);

ShowWindow(hWnd, SW_SHOWMAXIMIZED);

UpdateWindow(hWnd);

MSG msg;
 while( GetMessage(&msg, NULL, 0 , 0) )
 {
 TranslateMessage(&msg);
 DispatchMessage(&msg);
 }

 return msg.wParam;
}
LRESULT CALLBACK WindowProc(
 __in HWND hWnd,
 __in UINT uMsg,
 __in WPARAM wParam,
 __in LPARAM lParam
)
{
 HDC hDC;
 RECT rect;
 PAINTSTRUCT ps;

switch(uMsg)
 {
 case WM_CREATE:
 {
 SetTimer(hWnd, ID_TIMER, 100, NULL);
 }break;

case WM_TIMER:
 {
 InvalidateRect(hWnd, NULL, TRUE); //just refresh the window
 }break;

case WM_PAINT:
 {
 hDC = BeginPaint(hWnd, &ps);

GetClientRect(hWnd, &rect); //get all the screen to paint
 HBRUSH hBrush = CreateSolidBrush( RGB(rand()%256,rand()%256,rand()%256) ); //create the random color to paint
 HBRUSH hOldBrush = (HBRUSH)SelectObject(hDC, hBrush);

ShowCursor(FALSE); //hide the cursor

FillRect(hDC, &rect, hBrush); //paint all the screen with a randomly colorful brush

SelectObject(hDC, hOldBrush);
 DeleteObject(hBrush); //release the resource
 EndPaint(hWnd, &ps);
 }break;

case WM_CHAR: //allow pressing any button to exit
 {
 if( VK_ESCAPE & wParam )
 {
 //MessageBeep( MB_ICONASTERISK );
 DestroyWindow(hWnd);
 }
 }

case WM_DESTROY:
 {
 KillTimer(hWnd, ID_TIMER);
 PostQuitMessage(0);
 }break;

default:
 return DefWindowProc(hWnd, uMsg, wParam,lParam);
 }
}

</code></pre>

## 总结

里面用到了Win32 API，如创建窗口、计时器回调函数和消息响应什么的，至于屏幕保护程序是否只需写成exe我也没去深究了。

两年以后再看到这篇文章，已经不做Windows开发了。
