import sys
import os
from textwrap import dedent

# TODO: pull the template from templates/virtualbox_in?
def makeIterationTemplate(projectFolder, url, iteration):
    template = """<?xml version="1.0"?>

<input_template>

    <file_info>
        <number>0</number>
        <sticky/>
        <no_delete/>
        <gzip/>
        <gzipped_nbytes>5274728227</gzipped_nbytes>
        <url>{url}</url>
        <md5_cksum>67e8b22c80ea31ed7dcc98452f0e68ed 10159652864</md5_cksum>
        <nbytes>10 159 652 864</nbytes>
    </file_info>
    <file_info>
        <number>1</number>
        <no_delete/>
    </file_info>
    <file_info>
        <number>2</number>
        <no_delete/>
    </file_info>
    <file_info>
        <number>3</number>
        <no_delete/>
    </file_info>
    <file_info>
        <number>4</number>
        <no_delete/>
    </file_info>
    <file_info>
        <number>5</number>
        <no_delete/>
    </file_info>
    <file_info>
        <number>6</number>
        <no_delete/>
    </file_info>
    <file_info>
        <number>7</number>
        <no_delete/>
    </file_info>
    <file_info>
        <number>8</number>
        <no_delete/>
    </file_info>
    
    <workunit>
        <file_ref>
            <file_number>0</file_number>
            <open_name>hostvm_learning.vdi</open_name>
        </file_ref>
        <file_ref>
            <file_number>1</file_number>
            <open_name>vbox_job.xml</open_name>
            <copy_file/>
        </file_ref>
        <file_ref>
            <file_number>2</file_number>
            <open_name>shared/boinc_app</open_name>
            <copy_file/>
        </file_ref>
        <file_ref>
            <file_number>3</file_number>
            <open_name>shared/sharedModel.h5</open_name>
            <copy_file/>
        </file_ref>
        <file_ref>
            <file_number>4</file_number>
            <open_name>shared/main.py</open_name>
            <copy_file/>
        </file_ref>
        <file_ref>
            <file_number>5</file_number>
            <open_name>shared/model.py</open_name>
            <copy_file/>
        </file_ref>
        <file_ref>
            <file_number>6</file_number>
            <open_name>shared/nodeLogger.py</open_name>
            <copy_file/>
        </file_ref>
        <file_ref>
            <file_number>7</file_number>
            <open_name>shared/cfg_1.json</open_name>
            <copy_file/>
        </file_ref>
        <file_ref>
            <file_number>8</file_number>
            <open_name>shared/globalModelWeights_{iteration}.pkl</open_name>
            <copy_file/>
        </file_ref>
    </workunit>
    
</input_template>
    """
    newTemplate = dedent(template).format(iteration=iteration, url=url)
    filename = os.path.join("thesis/model/iterationTemplates/", f"virtualbox_in_{iteration}")
    '''
    <file_info>
        <number>0</number>
        <sticky/>
        <no_delete/>
        <gzip/>
        <gzipped_nbytes>5274728227</gzipped_nbytes>
        <url>http://109.63.253.178/remote/</url>
        <md5_cksum>67e8b22c80ea31ed7dcc98452f0e68ed 10159652864</md5_cksum>
        <nbytes>10159652864</nbytes>
    </file_info>
    
    
    <file_info>
        <number>9</number>
        <no_delete/>
        <gzip/>
        <gzipped_nbytes>464</gzipped_nbytes>
        <url>http://109.63.253.178/remote/</url>
        <md5_cksum>b9b242eb374df9087bdaaca7d719dd75</md5_cksum>
        <nbytes>1056</nbytes>
    </file_info>
    
    <file_ref>
            <file_number>9</file_number>
            <open_name>shared/output.txt</open_name>
            <copy_file/>
        </file_ref>
    '''

    with open(os.path.join(projectFolder, filename), "w") as f:
        f.write(newTemplate)
    return filename

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Error: expecting three arguments - projectFolderPath, remote_url and iteration number")
        sys.exit(1)
    
    projectFolder = sys.argv[1]
    iteration = sys.argv[2]
    url = sys.argv[3]
    makeIterationTemplate(projectFolder, url, iteration)
