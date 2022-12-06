LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE := MJPdfReader
LOCAL_SRC_FILES := MJPdfReader.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
LOCAL_CERTIFICATE := PRESIGNED

LOCAL_OPTIONAL_USES_LIBRARIES := \
    androidx.window.extensions \
    androidx.window.sidecar
include $(BUILD_PREBUILT)
