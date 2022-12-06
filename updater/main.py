import urllib.request
from os import path

import certificates
import git
from sources import ApkRelease, fdroid_recommended_release


def update_if_needed(module: str, release: ApkRelease):
    module_dir = path.abspath(path.join(path.dirname(__file__), '..', module))
    with open(path.join(module_dir, '.version_code'), 'r+') as version_code_file:
        version_code = int(version_code_file.read())
        if version_code < release.version_code:
            print('updating {} to {}'.format(module, release.version_name))
            apk_filename = path.join(module_dir, '{}.apk'.format(module))

            old_sig = certificates.get_apk_certificate(apk_filename)

            print('downloading {} ...'.format(release.download_url))
            urllib.request.urlretrieve(release.download_url, apk_filename)

            new_sig = certificates.get_apk_certificate(apk_filename)
            if old_sig != new_sig:
                raise Exception('Signature mismatch for {} old sig: {} new sig: {}'.format(module, old_sig, new_sig))

            version_code_file.seek(0)
            version_code_file.write(str(release.version_code))
            version_code_file.truncate()
            version_code_file.close()

            print('commit and push...')
            git.add_commit_push(module_dir, 'Update {} to {}'.format(module, release.version_name))

        elif version_code > release.version_code:
            print('{} ahead of suggested version ({} > {})'.format(module, version_code, release.version_code))
        elif version_code == release.version_code:
            print('{} up to date.'.format(module))

fdroid_main_repo = 'https://www.f-droid.org/repo'
fdroid_microg_repo = 'https://microg.org/fdroid/repo'
fdroid_izzy_repo = 'https://apt.izzysoft.de/fdroid/repo'
fdroid_divestos = 'https://divestos.org/fdroid/official'

update_if_needed('AuroraStore', fdroid_recommended_release(fdroid_main_repo, 'com.aurora.store'))
update_if_needed('AvesLibre', fdroid_recommended_release(fdroid_main_repo, 'deckers.thibault.aves.libre'))
update_if_needed('Droidify', fdroid_recommended_release(fdroid_main_repo, 'com.looker.droidify'))
update_if_needed('MJPdfReader', fdroid_recommended_release(fdroid_izzy_repo, 'com.gitlab.mudlej.MjPdfReader'))
update_if_needed('Mull', fdroid_recommended_release(fdroid_divestos_repo, 'us.spotco.fennec_dos'))
update_if_needed('OpenCalc', fdroid_recommended_release(fdroid_main_repo, 'com.darkempire78.opencalculator'))
