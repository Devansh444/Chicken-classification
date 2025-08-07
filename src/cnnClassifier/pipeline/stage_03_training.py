from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.training import Training
from cnnClassifier import logger



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Prepare callbacks
        prepare_callbacks = PrepareCallback(config=config.get_prepare_callback_config())
        callback_list    = prepare_callbacks.get_tb_ckpt_callbacks()

        # Training
        training = Training(config=config.get_training_config())
        training.get_base_model()           # loads & recompiles with run_eagerly=True
        training.train_valid_generator()    # sets up your ImageDataGenerators
    
        training.train(callback_list=callback_list)  # kicks off .fit()





if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        
