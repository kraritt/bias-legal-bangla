MODEL_NAME="csebuetnlp/banglabert"
DATA_PATH='dataset/annotate_filled.json'
MODEL_OUTPUT_DIR="fine-tuned-model"
NUM_CLASSES=2
BATCH_SIZE=32
N_EPOCHS=20
LR=1e-5
DEVICE='5'
SEED=42


python train.py \
    --model_name ${MODEL_NAME} \
    --data_path ${DATA_PATH} \
    --model_output_dir ${MODEL_OUTPUT_DIR} \
    --num_classes ${NUM_CLASSES} \
    --batch_size ${BATCH_SIZE} \
    --n_epochs ${N_EPOCHS} \
    --lr ${LR} \
    --device ${DEVICE} \
    --seed ${SEED}

