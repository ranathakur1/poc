from google.cloud import storage
import kfp.dsl as dsl
import kfp.gcp as gcp
import kfp.components as comp

def_project_id = 'test'

# def_output_gcs_path=test_rana

@dsl.pipeline(name='testflow', description='transform test pipeline')
def pipe(project_id=def_project_id,param1='param1'):
    common_args = [
        'target', 'trans1',
        '--param1', param1,
    ]


    writecsv = dsl.ContainerOp(
        name='writeCSV',
        image='gcr.io/glowing-harmony-291618/pddkube',
        command=['python', 'filewrite.py'],
        arguments=common_args,
    )


    readbq = dsl.ContainerOp(
        name='readBigQuery',
        image='gcr.io/glowing-harmony-291618/pddkube',
        command=['python', 'readbq.py'],
        arguments=common_args,
    )
    readbq.after(writecsv)


    dataupdation = dsl.ContainerOp(
        name='updatetBigTable',
        image='gcr.io/glowing-harmony-291618/pddkube',
        command=['python', 'addrowbt.py'],
        arguments=common_args,
    )
    dataupdation.after(readbq)



if __name__ == '__main__':
    import kfp.compiler as compiler

    compiler.Compiler().compile(pipe, 'pipeline.tar.gz')
