LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := AvesLibre
LOCAL_SRC_FILES := AvesLibre.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_PRODUCT_MODULE := true

LOCAL_OVERRIDES_PACKAGES := \
    Gallery2 \
    AudioFX

LOCAL_OPTIONAL_USES_LIBRARIES := \
    androidx.window.extensions \
    androidx.window.sidecar \
    org.apache.http.legacy
include $(BUILD_PREBUILT)