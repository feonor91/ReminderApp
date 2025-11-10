#!/usr/bin/env python3
"""
Создает полный Xcode проект со всеми файлами
Запустите на Mac после установки всех зависимостей
"""

import os
import sys
import uuid
from pathlib import Path

def generate_uuid():
    """Генерирует UUID в формате Xcode"""
    return ''.join(uuid.uuid4().hex.upper()[:24])

def get_mp3_files():
    """Получает список MP3 файлов"""
    app_dir = Path(__file__).parent / "ReminderApp"
    mp3_files = sorted(app_dir.glob("*.mp3"))
    return [f.name for f in mp3_files]

def create_project_pbxproj():
    """Создает файл project.pbxproj"""
    
    mp3_files = get_mp3_files()
    print(f"Found {len(mp3_files)} MP3 files")
    
    # Генерируем UUID для всех компонентов
    project_uuid = generate_uuid()
    target_uuid = generate_uuid()
    build_config_list_uuid = generate_uuid()
    debug_config_uuid = generate_uuid()
    release_config_uuid = generate_uuid()
    main_group_uuid = generate_uuid()
    products_group_uuid = generate_uuid()
    app_group_uuid = generate_uuid()
    resources_phase_uuid = generate_uuid()
    sources_phase_uuid = generate_uuid()
    frameworks_phase_uuid = generate_uuid()
    
    # UUID для файлов
    app_delegate_uuid = generate_uuid()
    scene_delegate_uuid = generate_uuid()
    view_controller_uuid = generate_uuid()
    notification_manager_uuid = generate_uuid()
    info_plist_uuid = generate_uuid()
    assets_uuid = generate_uuid()
    
    # UUID для MP3 файлов
    mp3_file_refs = {}
    mp3_build_files = {}
    for mp3_file in mp3_files:
        mp3_file_refs[mp3_file] = generate_uuid()
        mp3_build_files[mp3_file] = generate_uuid()
    
    # UUID для Swift файлов в BuildFile
    app_delegate_build = generate_uuid()
    scene_delegate_build = generate_uuid()
    view_controller_build = generate_uuid()
    notification_manager_build = generate_uuid()
    
    # UUID для Info.plist в BuildFile
    info_plist_build = generate_uuid()
    
    # Создаем содержимое project.pbxproj
    pbxproj_content = f'''// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{
	}};
	objectVersion = 56;
	objects = {{

/* Begin PBXBuildFile section */
		{app_delegate_build} /* AppDelegate.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {app_delegate_uuid} /* AppDelegate.swift */; }};
		{scene_delegate_build} /* SceneDelegate.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {scene_delegate_uuid} /* SceneDelegate.swift */; }};
		{view_controller_build} /* ViewController.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {view_controller_uuid} /* ViewController.swift */; }};
		{notification_manager_build} /* NotificationManager.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {notification_manager_uuid} /* NotificationManager.swift */; }};
		{info_plist_build} /* Info.plist in Resources */ = {{isa = PBXBuildFile; fileRef = {info_plist_uuid} /* Info.plist */; }};
'''
    
    # Добавляем MP3 файлы в BuildFile
    for mp3_file, build_uuid in mp3_build_files.items():
        pbxproj_content += f'''		{build_uuid} /* {mp3_file} in Resources */ = {{isa = PBXBuildFile; fileRef = {mp3_file_refs[mp3_file]} /* {mp3_file} */; }};
'''
    
    pbxproj_content += '''/* End PBXBuildFile section */

/* Begin PBXFileReference section */
'''
    
    # Добавляем файлы
    pbxproj_content += f'''		{app_delegate_uuid} /* AppDelegate.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AppDelegate.swift; sourceTree = "<group>"; }};
		{scene_delegate_uuid} /* SceneDelegate.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SceneDelegate.swift; sourceTree = "<group>"; }};
		{view_controller_uuid} /* ViewController.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ViewController.swift; sourceTree = "<group>"; }};
		{notification_manager_uuid} /* NotificationManager.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = NotificationManager.swift; sourceTree = "<group>"; }};
		{info_plist_uuid} /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; }};
		{assets_uuid} /* Assets.xcassets */ = {{isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; }};
		{target_uuid} /* ReminderApp.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = ReminderApp.app; sourceTree = BUILT_PRODUCTS_DIR; }};
'''
    
    # Добавляем MP3 файлы
    for mp3_file, file_uuid in mp3_file_refs.items():
        pbxproj_content += f'''		{file_uuid} /* {mp3_file} */ = {{isa = PBXFileReference; lastKnownFileType = audio.mp3; path = "{mp3_file}"; sourceTree = "<group>"; }};
'''
    
    pbxproj_content += f'''/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		{frameworks_phase_uuid} /* Frameworks */ = {{
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		{main_group_uuid} = {{
			isa = PBXGroup;
			children = (
				{app_group_uuid} /* ReminderApp */,
				{products_group_uuid} /* Products */,
			);
			sourceTree = "<group>";
		}};
		{app_group_uuid} /* ReminderApp */ = {{
			isa = PBXGroup;
			children = (
				{app_delegate_uuid} /* AppDelegate.swift */,
				{scene_delegate_uuid} /* SceneDelegate.swift */,
				{view_controller_uuid} /* ViewController.swift */,
				{notification_manager_uuid} /* NotificationManager.swift */,
				{info_plist_uuid} /* Info.plist */,
				{assets_uuid} /* Assets.xcassets */,
'''
    
    # Добавляем MP3 файлы в группу
    for mp3_file, file_uuid in mp3_file_refs.items():
        pbxproj_content += f'''				{file_uuid} /* {mp3_file} */,
'''
    
    pbxproj_content += f'''			);
			path = ReminderApp;
			sourceTree = "<group>";
		}};
		{products_group_uuid} /* Products */ = {{
			isa = PBXGroup;
			children = (
				{target_uuid} /* ReminderApp.app */,
			);
			name = Products;
			sourceTree = "<group>";
		}};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		{target_uuid} /* ReminderApp */ = {{
			isa = PBXNativeTarget;
			buildConfigurationList = {build_config_list_uuid} /* Build configuration list for PBXNativeTarget "ReminderApp" */;
			buildPhases = (
				{sources_phase_uuid} /* Sources */,
				{frameworks_phase_uuid} /* Frameworks */,
				{resources_phase_uuid} /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = ReminderApp;
			productName = ReminderApp;
			productReference = {target_uuid} /* ReminderApp.app */;
			productType = "com.apple.product-type.application";
		}};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		{project_uuid} /* Project object */ = {{
			isa = PBXProject;
			attributes = {{
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 1500;
				LastUpgradeCheck = 1500;
				TargetAttributes = {{
					{target_uuid} = {{
						CreatedOnToolsVersion = 15.0;
					}};
				}};
			}};
			buildConfigurationList = {generate_uuid()} /* Build configuration list for PBXProject "ReminderApp" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = {main_group_uuid};
			productRefGroup = {products_group_uuid} /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				{target_uuid} /* ReminderApp */,
			);
		}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		{resources_phase_uuid} /* Resources */ = {{
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				{info_plist_build} /* Info.plist in Resources */,
'''
    
    # Добавляем MP3 файлы в Resources
    for mp3_file, build_uuid in mp3_build_files.items():
        pbxproj_content += f'''				{build_uuid} /* {mp3_file} in Resources */,
'''
    
    pbxproj_content += f'''			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		{sources_phase_uuid} /* Sources */ = {{
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				{app_delegate_build} /* AppDelegate.swift in Sources */,
				{scene_delegate_build} /* SceneDelegate.swift in Sources */,
				{view_controller_build} /* ViewController.swift in Sources */,
				{notification_manager_build} /* NotificationManager.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		{debug_config_uuid} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = YES;
				GCC_C_LANGUAGE_STANDARD = gnu17;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = "DEBUG $(inherited)";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			}};
			name = Debug;
		}};
		{release_config_uuid} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = YES;
				GCC_C_LANGUAGE_STANDARD = gnu17;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				SDKROOT = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				VALIDATE_PRODUCT = YES;
			}};
			name = Release;
		}};
		{generate_uuid()} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = ReminderApp/Info.plist;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations = "UIInterfaceOrientationPortrait UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.reminderapp;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			}};
			name = Debug;
		}};
		{generate_uuid()} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = ReminderApp/Info.plist;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations = "UIInterfaceOrientationPortrait UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.reminderapp;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			}};
			name = Release;
		}};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		{build_config_list_uuid} /* Build configuration list for PBXNativeTarget "ReminderApp" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{generate_uuid()} /* Debug */,
				{generate_uuid()} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
		{generate_uuid()} /* Build configuration list for PBXProject "ReminderApp" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{debug_config_uuid} /* Debug */,
				{release_config_uuid} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
/* End XCConfigurationList section */
	}};
	rootObject = {project_uuid} /* Project object */;
}}
'''
    
    return pbxproj_content

def main():
    print("Creating Xcode project for New Year Reminder App\n")
    
    project_dir = Path(__file__).parent
    xcodeproj_dir = project_dir / "ReminderApp.xcodeproj"
    
    if xcodeproj_dir.exists():
        response = input(f"Project {xcodeproj_dir} already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Cancelled")
            return 1
    
    # Создаем структуру проекта
    print("Creating project structure...")
    xcodeproj_dir.mkdir(exist_ok=True)
    
    # Создаем project.pbxproj
    print("Creating project.pbxproj...")
    pbxproj_content = create_project_pbxproj()
    
    pbxproj_path = xcodeproj_dir / "project.pbxproj"
    with open(pbxproj_path, 'w', encoding='utf-8') as f:
        f.write(pbxproj_content)
    
    print(f"Project created: {xcodeproj_dir}")
    print("\nNext steps:")
    print("   1. Open project in Xcode: open ReminderApp.xcodeproj")
    print("   2. Configure Signing & Capabilities (select Team)")
    print("   3. Connect iPhone")
    print("   4. Product -> Run (Cmd+R) to install on device")
    print("   OR")
    print("   5. Run: ./build_ipa.sh to build IPA")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

