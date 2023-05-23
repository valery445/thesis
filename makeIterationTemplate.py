import sys
import os
from textwrap import dedent

def makeIterationTemplate(projectFolder, iteration):
    template = """<?xml version="1.0"?>

<input_template>

    <file_info>
        <number>0</number>
        <sticky/>
        <no_delete/>
        <gzip/>
        <gzipped_nbytes>5 274 728 227</gzipped_nbytes>
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
    newTemplate = dedent(template).format(iteration=iteration)
    filename = os.path.join("model/iterationTemplates/", f"virtualbox_in_{iteration}")

    with open(os.path.join(projectFolder, filename), "w") as f:
        f.write(newTemplate)
    return filename

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: expecting two arguments - projectFolderPath and iteration number")
        sys.exit(1)
    
    projectFolder = sys.argv[1]
    iteration = sys.argv[2]
    makeIterationTemplate(projectFolder, iteration)
