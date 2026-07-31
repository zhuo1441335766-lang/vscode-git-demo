adb wait-for-device
adb root
adb wait-for-device
adb remount
adb shell mkdir system/priv-app/XpFactoryTest/
adb shell mkdir system/priv-app/XpFactoryTest/lib/
adb shell mkdir system/priv-app/XpFactoryTest/lib/arm64/
adb shell rm -rf /system/priv-app/XpFactoryTest/oat/
adb push .\XpFactoryTest.apk /system/priv-app/XpFactoryTest/
adb push .\lib\arm64\libpso.so system/priv-app/XpFactoryTest/lib/arm64/
adb push .\lib\arm64\libXpPso.so system/priv-app/XpFactoryTest/lib/arm64/
adb push .\lib\arm64\libudsSecurityLuaEnc.so system/priv-app/XpFactoryTest/lib/arm64/
adb push .\lib\arm64\libsentry.so system/priv-app/XpFactoryTest/lib/arm64/
adb push .\lib\arm64\libsentry-android.so system/priv-app/XpFactoryTest/lib/arm64/
adb shell rm -rf /data/app/com.xiaopeng.factory*
adb reboot
pause