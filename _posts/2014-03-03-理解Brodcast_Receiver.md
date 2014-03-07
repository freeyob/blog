---
layout: post
title: 理解Brodcast_Receiver
tags:
- android
categories:
- android
---

### 用来干麻的？即为什么要用BrocastReceriver。  
Android中用来监听系统或者别的应用的组件。  

### 生命周期
其生命周期非常短暂，即对象构造，然后执行onReceive()，就销毁对象。  
当onReceive()执行中，所在进程为前台进程。所以如果执行时间过长（大于10秒），就会被强行关闭。而且其在主线程中构造，执行时间过长，会拖慢界面。所以，onReceive()执行要快速，避免过多应用进程成为前台进程。  
在BrodcastReceiver中一般进行简单的判断，然后通过Notification通知用户或者Context.startActivity()交给界面组件去处理或者交给服务组件去处理。  

### 绑定  
监听器使用方式分为两种：  
1. 冷插拔，就是在xml中配置的，适合低频率事件。它存在于系统的整个生命周期。因为应用的安装管理服务，在安装应用的时候会扫描xml中的所有BrodcastReceiver信息。  
2. 热插拔，代码中继承了BrodcastReceiver,适合高频率事件。它的生命周期是registerReceiver()和unregisterReceiver()之间。对于频性时间，又不必时时监听的可以用这两个函数来调整它的生命周期。  

### 机制  
组件管理服务收到广播，会根据安装管理服务和registerReceiver()的信息筛选，去依次构造BrocastReceriver对象并执行onRecerive()方法，然后销毁对象。  
### 发送广播  
- 并发发送 sendBrodcast();注册了都会收到。比如，开机广播。
- 有序发送 sendOrderedBrodcast();按照优先级形成一个链，依次处理，排在前面的可以通过abortBrocast()阻止向下传播。还可以加入数据setResult()，后边的可以通过getResultData()收到。  
