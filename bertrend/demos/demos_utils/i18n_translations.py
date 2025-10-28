#  Copyright (c) 2024, RTE (https://www.rte-france.com)
#  See AUTHORS.txt
#  SPDX-License-Identifier: MPL-2.0
#  This file is part of BERTrend.

# Translation dictionaries for demos_utils
TRANSLATIONS = {
    "ctrl_enter": {
        "fr": "CTRL + Entrée pour mettre à jour",
        "en": "CTRL + Enter to update",
        "zh": "Ctrl + Enter 更新"
    },
    "select_language": {
        "fr": "Choisir une langue",
        "en": "Select Language",
        "zh": "选择语言"
    },
    "embedding_model": {
        "fr": "Modèle d'embedding",
        "en": "Embedding Model",
        "zh": "嵌入模型"
    },
    "embedding_service_url": {
        "fr": "URL du service d'embedding",
        "en": "Embedding service URL",
        "zh": "嵌入服务URL"
    },
    "embedding_hyperparameters": {
        "fr": "Paramètres d'embedding",
        "en": "Embedding settings",
        "zh": "嵌入参数设置"
    },
    "embedding_service": {
        "fr": "Service d'embedding",
        "en": "Embedding Service",
        "zh": "嵌入服务"
    },
    "bertopic_hyperparameters": {
        "fr": "Hyperparamètres BERTopic",
        "en": "BERTopic Hyperparameters",
        "zh": "BERTopic超参数"
    },
    "bertrend_hyperparameters": {
        "fr": "Hyperparamètres BERTrend",
        "en": "BERTrend Hyperparameters",
        "zh": "BERTrend超参数"
    },
    "embeddings_calculated_message": {
        "fr": "Embeddings calculés avec succès !",
        "en": "Embeddings calculated successfully!",
        "zh": "嵌入计算成功！"
    },
    "no_embeddings_warning_message": {
        "fr": "Veuillez vectoriser les données et entraîner les modèles avant de procéder à l'analyse.",
        "en": "Please embed data and train models before proceeding to analysis.",
        "zh": "请先进行数据嵌入和模型训练，然后再进行分析。"
    },
    "model_training_complete_message": {
        "fr": "Entraînement du modèle terminé !",
        "en": "Model training complete!",
        "zh": "模型训练完成！"
    },
    "no_data_after_preprocessing_message": {
        "fr": "Aucune donnée disponible après prétraitement. Veuillez vérifier les fichiers sélectionnés et les options de prétraitement.",
        "en": "No data available after preprocessing. Please check the selected files and preprocessing options.",
        "zh": "预处理后无可用数据。请检查所选文件及预处理选项。"
    },
    "select_from_local_storage": {
        "fr": "Selection de jeux de données à partir du stockage local (.xlsx, .csv, .json, .jsonl, .parquet)",
        "en": "Select dataset from local storage (.xlsx, .csv, .json, .jsonl, .parquet)",
        "zh": "从本地存储选择数据集 (.xlsx, .csv, .json, .jsonl, .parquet)"
    },
    "select_from_remote_storage": {
        "fr": "Selection de jeux de données sur le serveur",
        "en": "Select one or more datasets from the server data",
        "zh": "从服务器数据中选择一个或多个数据集"
    },
    "data_loading": {
        "fr": "Chargement des données",
        "en": "Data loading",
        "zh": "数据加载"
    },
    "local_data": {
        "fr": "Données locales",
        "en": "Data from local storage",
        "zh": "本地存储数据"
    },
    "remote_data": {
        "fr": "Données sur le serveur",
        "en": "Data from server",
        "zh": "服务器数据"
    },
    "data_filtering": {
        "fr": "Filtrage des données",
        "en": "Data filtering",
        "zh": "数据筛选"
    },
    "embed_documents": {
        "fr": "Vectoriser les documents",
        "en": "Embed Documents",
        "zh": "文档嵌入"
    },
    "embedding_documents": {
        "fr": "Vectorisation des documents...",
        "en": "Embedding documents...",
        "zh": "正在嵌入文档..."
    },
    "no_dataset_warning": {
        "fr": "Veuillez sélectionner au moins un jeu de données pour continuer.",
        "en": "Please select at least one dataset to proceed.",
        "zh": "请选择至少一个数据集以继续。"
    },
    "error_loading_file": {
        "fr": "Erreur lors du chargement du fichier '{file_name}': {error}",
        "en": "Error while loading file '{file_name}': {error}",
        "zh": "加载文件 '{file_name}' 时出错: {error}"
    },
    "drag_drop_help": {
        "fr": "Glissez et déposez les fichiers à utiliser comme jeu de données dans cette zone",
        "en": "Drag and drop files to be used as dataset in this area",
        "zh": "将用作数据集的文件拖放到此区域"
    },
    "raw_documents_count": {
        "fr": "Nombre de documents dans les données brutes: **{count}**",
        "en": "Number of documents in raw data: **{count}**",
        "zh": "原始数据中的文档数量: **{count}**"
    },
    "minimum_characters": {
        "fr": "Nombre minimum de caractères",
        "en": "Minimum Characters",
        "zh": "最小字符数"
    },
    "minimum_characters_help": {
        "fr": "Nombre minimum de caractères que chaque document doit contenir.",
        "en": "Minimum number of characters each document must contain.",
        "zh": "每个文档必须包含的最小字符数。"
    },
    "sample_ratio": {
        "fr": "Ratio d'échantillonnage",
        "en": "Sample ratio",
        "zh": "采样比例"
    },
    "sample_ratio_help": {
        "fr": "Fraction des données brutes à utiliser pour calculer les sujets. Échantillonne aléatoirement les documents à partir des données brutes.",
        "en": "Fraction of raw data to use for computing topics. Randomly samples documents from raw data.",
        "zh": "用于计算主题的原始数据比例。从原始数据中随机采样文档。"
    },
    "split_by_paragraphs": {
        "fr": "Diviser le texte par paragraphes",
        "en": "Split text by paragraphs",
        "zh": "按段落分割文本"
    },
    "split_option_yes": {
        "fr": "oui",
        "en": "yes",
        "zh": "是"
    },
    "split_option_no": {
        "fr": "non",
        "en": "no",
        "zh": "否"
    },
    "split_option_enhanced": {
        "fr": "amélioré",
        "en": "enhanced",
        "zh": "增强"
    },
    "split_help": {
        "fr": "'Pas de division': Pas de division sur les documents ; 'Division par paragraphes': Divise les documents en paragraphes ; 'Division améliorée': utilise une méthode plus avancée mais plus lente pour la division qui prend en compte la longueur d'entrée maximale du modèle d'embedding.",
        "en": "'No split': No splitting on the documents ; 'Split by paragraphs': Split documents into paragraphs ; 'Enhanced split': uses a more advanced but slower method for splitting that considers the embedding model's maximum input length.",
        "zh": "'不分割': 不对文档进行分割；'按段落分割': 将文档分割为段落；'增强分割': 使用更先进但较慢的分割方法，考虑嵌入模型的最大输入长度。"
    },
    "select_timeframe": {
        "fr": "Sélectionner la période",
        "en": "Select Timeframe",
        "zh": "选择时间范围"
    },
    "filtered_documents_count": {
        "fr": "Nombre de documents dans les données filtrées: **{count}**",
        "en": "Number of documents in filtered data: **{count}**",
        "zh": "筛选后数据中的文档数量: **{count}**"
    },
    "settings_and_controls": {
        "fr": "Paramètres et contrôles",
        "en": "Settings and Controls",
        "zh": "设置和控件"
    },
    "column_selection": {
        "fr": "Sélection des colonnes",
        "en": "Column Selection",
        "zh": "列选择"
    },
    "text_column_selection": {
        "fr": "Sélection de la colonne contenant le texte",
        "en": "Select Column Containing Text",
        "zh": "选择包含文本的列"
    },
    "timestamp_column_selection": {
        "fr": "Sélection de la colonne contenant l'horodatage",
        "en": "Select Column Containing Timestamp",
        "zh": "选择包含时间戳的列"
    },
}