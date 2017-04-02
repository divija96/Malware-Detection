import csv
import numpy as np 
import pandas as pd 
#For Non Standard
df=pd.read_csv('Feature2.csv')
f=open('TemporaryDictBenign','rU')
CsvHeaders= ['amazon.permission.COLLECT_METRICS','android.hardware.camera.autofocus','android.hardware.camera.flash','android.hardware.camera','android.net.conn.CONNECTIVITY_CHANGE','android.webkit.permission.PLUGIN','com.airbnb.android.permission.JPUSH_MESSAGE','com.amazon.android.permission.DOWNLOAD_WITHOUT_NOTIFICATION','com.amazon.dcp.config.permission.DYN_CONFIG_VALUES_UPDATED','com.amazon.dcp.messaging.permission.HANDLE_DEVICE_MESSAGE','com.amazon.dcp.metrics.permission.METRICS_PERMISSION','com.amazon.dcp.sso.permission.account.changed','com.amazon.dcp.sso.permission.AMAZON_ACCOUNT_PROPERTY','com.amazon.dcp.sso.permission.MANAGE_COR_PFM','com.amazon.dcp.sso.permission.USE_DEVICE_CREDENTIALS','com.amazon.identity.auth.device.perm.AUTH_SDK','com.amazon.identity.permission.CALL_AMAZON_DEVICE_INFORMATION_PROVIDER','com.amazon.identity.permission.CAN_CALL_MAP_INFORMATION_PROVIDER','com.amazon.identity.permission.GENERIC_IPC','com.amazon.kindle.socialsharing.PERMISSION_SHARE','com.amazon.permission.FORCE_AUTH_ACCT','com.anddoes.launcher.permission.UPDATE_COUNT','com.android.alarm.permission.GET_ALARM','com.android.alarm.permission.SET_ALARM','com.android.alarm.permission.SET_ALARM','com.android.chrome.TOS_ACKED','com.android.email.partnerprovider.PARTNER_PROVIDER','com.android.permission.mewidget_contact','com.android.vending.CHECK_LICENSE','com.apusapps.launcher.permission.APUS','com.apusapps.tools.notification.permission.NOTIFICATION','com.asus.filemanager.provider.OpenFileProvider.PERMISSION.WRITE','com.asus.vzwhelp.provider.permission','com.audible.hushpuppy.tablet.permission.COMPANION_MAPPING','com.chrome.permission.DEVICE_EXTRAS','com.contapps.android.permission.SHORTCUT','com.coolots.chatonv.permission.provider.LIVE_SHARE_CANADA','com.coolots.chatonv.permission.provider.LIVE_SHARE','com.coolots.permission.COOLOTS_CANADA','com.coolots.permission.COOLOTS','com.cyngn.browser.permission.WRITE_HOMEPAGE','com.domobile.applock.PERMISSON_STOP_WATCHDOG_AFTER_SCREEN_OFF','com.edjing.edjingdjturntable.permission.RATING','com.facebook.home.permission.WRITE_BADGES','com.facebook.mlite.BROADCAST','com.facebook.orca.permission.CROSS_PROCESS_BROADCAST_MANAGER','com.facebook.permission.prod.FB_APP_COMMUNICATION','com.flipdog.crypto.plugin.FLIPDOG_APPLICATION','com.google.android.apps.maps.permission.PREFETCH','com.google.android.apps.photos.permission.GOOGLE_PHOTOS','com.google.android.c2dm.intent.REGISTER','com.google.android.c2dm.permission.SEND','com.google.android.gallery3d.permission.GALLERY_PROVIDER','com.google.android.gallery3d.permission.PICASA_STORE','com.google.android.gm.email.permission.GET_WIDGET_UPDATE','com.google.android.gm.permission.AUTO_SEND','com.google.android.gm.permission.BROADCAST_INTERNAL','com.google.android.gm.permission.WRITE_GMAIL','com.google.android.gms.permission.ACTIVITY_RECOGNITION','com.google.android.gms.permission.CAR_SPEED','com.google.android.googleapps.permission.GOOGLE_AUTH.mail','com.google.android.googleapps.permission.GOOGLE_AUTH','com.htc.launcher.permission.UPDATE_SHORTCUT','com.htc.permission.APP_PLATFORM','com.huawei.android.launcher.permission.CHANGE_BADGE','com.icq.mobile.client.permission.GET_SETTINGS','com.jio.mhood.jionet.action.REFRESHSSO','com.lab126.downloads.DOWNLOAD_CALLBACK_SVC','com.lab126.downloads.DOWNLOAD_SVC_CLIENT_CONNECT','com.majeur.launcher.permission.UPDATE_BADGE','com.meitu.permission.REMOTE_CONTROLLER','com.nimbuzz.permission.ExternalNimbuzzActions','com.openintents.notepad.WRITE_PERMISSION','com.qihoo.antivirus.update.permission.i18n_security_lite','com.qihoo.antivirus.update.permission.i18n_security','com.qihoo.security.lite.PERMISSION','com.qihoo.security.PERMISSION','com.qihoo360.screenlock.permission.WRITE_LOCAL_THEME','com.samsung.android.providers.context.permission.WRITE_USE_APP_FEATURE_SURVEY','com.samsung.wmanager.ENABLE_NOTIFICATION','com.sec.android.app.factorymode.permission.KEYSTRING','com.sec.android.provider.badge.permission.WRITE','com.sec.chaton.error','com.sec.chaton.provider.WRITE_PERMISSION','com.sec.chaton.push.BROADCAST_PUSH_MESSAGE','com.sec.chaton.smsplugin.provider.WRITE_PERMISSION','com.sec.chaton','com.sec.enterprise.knox.MDM_CONTENT_PROVIDER','com.sec.spp.permission.TOKEN_13b9cdc89f21278b87e0488ad5efb298532ad60905603d81a5145b0a03ce869cca937166ae9a01578767a15e8a36b9cc849a1de35bdc3facc1512f316ef9d09467c514442069ec167c16a8c8e67a4c641fc8d4b6394660a151f95a04e5c397de36c8df48dfbe0d12c45e76e6ca5a21f595994dd136023407173f9b983e2fa208','com.sony.mobile.permission.SYSTEM_UI_VISIBILITY_EXTENSION','com.sonyericsson.home.permission.BROADCAST_BADGE','com.sonymobile.home.permission.PROVIDER_INSERT_BADGE','com.sonymobile.permission.CAMERA_ADDON','com.sygic.familywhere.android.permission.PUSH','com.tencent.ibg.joox.theme.permission','com.trendmicro.androidmup.MUP_PRODUCTS_COMMUNICATION','com.trendmicro.InternalBroadcast','com.winit.merucabs.broadcastpermission','huawei.android.permission.HW_SIGNATURE_OR_SYSTEM','huawei.android.permission.HW_SIGNATURE_OR_SYSTEM','org.apache.android.xmpp.permission.PAYMENT_BROADCAST_PERMISSION','pioneer.permission.appradio.ADVANCED_APPMODE','rockchip.permission.FULL_SCREEN','sstream.app.broadcast.SYNC_USER','sstream.app.StoryProvider.WRITE.PERMISSION']
Permissions=set()
DistinctPermissions=set()
AppsDictionary={}
for line in f:
	AppApk,AppPermissions=line.split(":")
	AppsDictionary[AppApk]=AppPermissions
	#print AppsDictionary
	#print

i=1
count=0
for AppApk in AppsDictionary: #For a particular app
	i=i+1
	PermString=AppsDictionary[AppApk]
	PermString=PermString[1:-2]
	PermsList=PermString.split(', ')
	#print PermsList
	for Perm in PermsList:# Permissions of the ith app		
		
		for header in CsvHeaders:
			#print header
			#print Perm[1:-1]
			#break
			if( not Perm.startswith("\'android.permission.")):
				if(Perm[1:-1]==header):	
					count=count+1				
					print "Yay!!"
					print AppApk
					df.loc[i,header]=1
					print i
					print header
					print Perm[1:-1]
					print df.loc[i,header]

df.fillna(0, inplace=True)				
df.to_csv('outNonStandardWholeBenign.csv')

#for row in cw:
#	App=AppsDictionary[row[0]]
#
#   row[3] = 4
#   writer.writerow(row)

