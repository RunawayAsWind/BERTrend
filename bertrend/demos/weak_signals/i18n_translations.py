#  Copyright (c) 2024, RTE (https://www.rte-france.com)
#  See AUTHORS.txt
#  SPDX-License-Identifier: MPL-2.0
#  This file is part of BERTrend.

# 弱信号演示的翻译字典
TRANSLATIONS = {
    # app.py 翻译
    "page_title": {
        "fr": "BERTrend - Démo d'analyse rétrospective de tendances",
        "en": "BERTrend - Trend Retrospective Analysis demo",
        "zh": "BERTrend - 趋势回顾分析演示",
    },
    "data_loading": {
        "fr": "Chargement des données",
        "en": "Data Loading",
        "zh": "数据加载",
    },
    "model_training": {
        "fr": "Entraînement du modèle",
        "en": "Model Training",
        "zh": "模型训练",
    },
    "results_analysis": {
        "fr": "Analyse des résultats",
        "en": "Results Analysis",
        "zh": "结果分析",
    },
    "state_management": {
        "fr": "Gestion de l'état",
        "en": "State Management",
        "zh": "状态管理",
    },
    "restore_previous_run": {
        "fr": "Restaurer l'exécution précédente",
        "en": "Restore Previous Run",
        "zh": "恢复之前的运行",
    },
    "purge_cache": {
        "fr": "Purger le cache",
        "en": "Purge Cache",
        "zh": "清理缓存",
    },
    "clear_session_state": {
        "fr": "Effacer l'état de la session",
        "en": "Clear session state",
        "zh": "清除会话状态",
    },
    "data_loading_and_preprocessing": {
        "fr": "Chargement et prétraitement des données",
        "en": "Data Loading and Preprocessing",
        "zh": "数据加载和预处理",
    },
    "documents_per_timestamp": {
        "fr": "Documents par horodatage",
        "en": "Documents per Timestamp",
        "zh": "每个时间戳的文档数",
    },
    "granularity": {
        "fr": "Granularité",
        "en": "Granularity",
        "zh": "粒度",
    },
    "select_timestamp": {
        "fr": "Sélectionner l'horodatage",
        "en": "Select Timestamp",
        "zh": "选择时间戳",
    },
    "enter_zeroshot_topics": {
        "fr": "Entrez les sujets zero-shot (séparés par /)",
        "en": "Enter zero-shot topics (separated by /)",
        "zh": "输入零样本主题（用/分隔）",
    },
    "train_models": {
        "fr": "Entraîner les modèles",
        "en": "Train Models",
        "zh": "训练模型",
    },
    "training_models": {
        "fr": "Entraînement des modèles...",
        "en": "Training models...",
        "zh": "正在训练模型...",
    },
    "topic_overview": {
        "fr": "Aperçu des sujets",
        "en": "Topic Overview",
        "zh": "主题概览",
    },
    "zeroshot_weak_signal_trends": {
        "fr": "Tendances des signaux faibles zero-shot",
        "en": "Zero-shot Weak Signal Trends",
        "zh": "零样本弱信号趋势",
    },
    "popularity_of_zeroshot_topics": {
        "fr": "Popularité des sujets zero-shot",
        "en": "Popularity of Zero-Shot Topics",
        "zh": "零样本主题的流行度",
    },
    "timestamp": {
        "fr": "Horodatage",
        "en": "Timestamp",
        "zh": "时间戳",
    },
    "popularity": {
        "fr": "Popularité",
        "en": "Popularity",
        "zh": "流行度",
    },
    "zeroshot_topics_data_saved": {
        "fr": "Données des sujets zero-shot sauvegardées dans {json_file_path}",
        "en": "Zeroshot topics data saved to {json_file_path}",
        "zh": "零样本主题数据已保存到 {json_file_path}",
    },
    "topic_size_evolution": {
        "fr": "Évolution de la taille des sujets",
        "en": "Topic Size Evolution",
        "zh": "主题规模演变",
    },
    "topic_popularity_evolution": {
        "fr": "Évolution de la popularité des sujets",
        "en": "Topic Popularity Evolution",
        "zh": "主题流行度演变",
    },
    "signal_analysis": {
        "fr": "Analyse du signal",
        "en": "Signal Analysis",
        "zh": "信号分析",
    },
    "enter_topic_number": {
        "fr": "Entrez un numéro de sujet pour l'examiner de plus près :",
        "en": "Enter a topic number to take a closer look:",
        "zh": "输入主题编号以仔细查看：",
    },
    "analyze_signal": {
        "fr": "Analyser le signal",
        "en": "Analyze signal",
        "zh": "分析信号",
    },
    "error_generating_signal_summary": {
        "fr": "Erreur lors de la génération du résumé du signal : {e}",
        "en": "Error while trying to generate signal summary: {e}",
        "zh": "生成信号摘要时出错：{e}",
    },
    "error_embedding_documents": {
        "fr": "Une erreur s'est produite lors de la vectorisation : {e}",
        "en": "An error occurred while embedding documents: {e}",
        "zh": "嵌入文档时发生错误：{e}",
    },
    "topic_evolution": {
        "fr": "Évolution des sujets",
        "en": "Topic Evolution",
        "zh": "主题演变",
    },
    "newly_emerged_topics": {
        "fr": "Sujets nouvellement apparus",
        "en": "Newly Emerged Topics",
        "zh": "新出现的主题",
    },
    "retrieve_topic_counts": {
        "fr": "Récupérer les comptages de sujets",
        "en": "Retrieve Topic Counts",
        "zh": "检索主题计数",
    },
    "retrieving_topic_counts": {
        "fr": "Récupération des comptages de sujets...",
        "en": "Retrieving topic counts...",
        "zh": "正在检索主题计数...",
    },
    "state_saved_message": {
        "fr": "État de l'application sauvegardé.",
        "en": "Application state saved.",
        "zh": "应用程序状态已保存。",
    },
    "state_restored_message": {
        "fr": "État de l'application restauré.",
        "en": "Application state restored.",
        "zh": "应用程序状态已恢复。",
    },
    "models_saved_message": {
        "fr": "Modèles sauvegardés.",
        "en": "Models saved.",
        "zh": "模型已保存。",
    },
    "models_restored_message": {
        "fr": "Modèles restaurés.",
        "en": "Models restored.",
        "zh": "模型已恢复。",
    },
    "model_merging_complete_message": {
        "fr": "Fusion des modèles terminée !",
        "en": "Model merging complete!",
        "zh": "模型合并完成！",
    },
    "topic_counts_saved_message": {
        "fr": "Comptages de sujets et de signaux sauvegardés dans {file_path}",
        "en": "Topic and signal counts saved to {file_path}",
        "zh": "主题和信号计数已保存到 {file_path}",
    },
    "cache_purged_message": {
        "fr": "Cache purgé.",
        "en": "Cache purged.",
        "zh": "缓存已清理。",
    },
    "progress_bar_description": {
        "fr": "Lots traités",
        "en": "Batches processed",
        "zh": "已处理的批次",
    },
    "no_data_warning": {
        "fr": "Aucune donnée disponible pour la granularité sélectionnée.",
        "en": "No data available for the selected granularity.",
        "zh": "所选粒度没有可用数据。",
    },
    "no_state_warning": {
        "fr": "Aucun état sauvegardé trouvé.",
        "en": "No saved state found.",
        "zh": "未找到保存的状态。",
    },
    "no_models_warning": {
        "fr": "Aucun modèle sauvegardé trouvé.",
        "en": "No saved models found.",
        "zh": "未找到保存的模型。",
    },
    "no_cache_warning": {
        "fr": "Aucun cache trouvé.",
        "en": "No cache found.",
        "zh": "未找到缓存。",
    },
    "embed_warning": {
        "fr": "Veuillez vectoriser les données avant de procéder à l'entraînement du modèle.",
        "en": "Please embed data before proceeding to model training.",
        "zh": "请在进行模型训练之前先嵌入数据。",
    },
    "embed_train_warning": {
        "fr": "Veuillez vectoriser les données et entraîner les modèles avant de procéder à l'analyse.",
        "en": "Please embed data and train models before proceeding to analysis.",
        "zh": "请在进行分析之前先嵌入数据并训练模型。",
    },
    "train_warning": {
        "fr": "Veuillez entraîner les modèles avant de procéder à l'analyse.",
        "en": "Please train models before proceeding to analysis.",
        "zh": "请在进行分析之前先训练模型。",
    },
    "merge_warning": {
        "fr": "Veuillez fusionner les modèles pour voir des analyses supplémentaires.",
        "en": "Please merge models to view additional analyses.",
        "zh": "请合并模型以查看其他分析。",
    },
    "topic_not_found_warning": {
        "fr": "Le sujet {topic_number} n'a pas été trouvé dans l'historique des fusions dans la fenêtre spécifiée.",
        "en": "Topic {topic_number} not found in the merge histories within the specified window.",
        "zh": "在指定窗口内的合并历史中未找到主题 {topic_number}。",
    },
    "no_granularity_warning": {
        "fr": "Valeur de granularité non trouvée.",
        "en": "Granularity value not found.",
        "zh": "未找到粒度值。",
    },
    "html_generation_failed_warning": {
        "fr": "La génération HTML a échoué. Affichage du markdown à la place.",
        "en": "HTML generation failed. Displaying markdown instead.",
        "zh": "HTML 生成失败。改为显示 Markdown。",
    },
    "search_topics_by_keywords": {
        "en": "Search topics by keyword:",
        "fr": "Recherche des sujets par mots-clés :",
        "zh": "按关键词搜索主题：",
    },
    "retrospective_period": {
        "en": "Retrospective Period (days)",
        "fr": "Période rétrospective (jours)",
        "zh": "回顾周期（天）",
    },
    "current_date": {
        "en": "Current date",
        "fr": "Date actuelle",
        "zh": "当前日期",
    },
    "current_date_help": {
        "en": "The earliest selectable date corresponds to the earliest timestamp when topics were merged (with the smallest possible value being the earliest timestamp in the provided data). The latest selectable date corresponds to the most recent topic merges, which is at most equal to the latest timestamp in the data minus the provided granularity.",
        "fr": "La date sélectionnable la plus ancienne correspond au premier horodatage où des sujets ont été fusionnés (avec la valeur minimale possible étant le premier horodatage dans les données fournies). La date sélectionnable la plus récente correspond aux fusions de sujets les plus récentes, qui est au plus égale au dernier horodatage dans les données moins la granularité fournie.",
        "zh": "最早可选日期对应于主题合并的最早时间戳（最小可能值是所提供数据中的最早时间戳）。最晚可选日期对应于最近的主题合并，最多等于数据中的最新时间戳减去所提供的粒度。",
    },
    "noise_threshold": {
        "en": "Noise Threshold : {value}",
        "fr": "Seuil de bruit : {value}",
        "zh": "噪声阈值：{value}",
    },
    "strong_signal_threshold": {
        "en": "Strong Signal Threshold : {value}",
        "fr": "Seuil de signal fort : {value}",
        "zh": "强信号阈值：{value}",
    },
    "weak_signals": {
        "en": "Weak Signals",
        "fr": "Signaux faibles",
        "zh": "弱信号",
    },
    "strong_signals": {
        "en": "Strong Signals",
        "fr": "Signaux forts",
        "zh": "强信号",
    },
    "noise": {
        "en": "Noise",
        "fr": "Bruit",
        "zh": "噪声",
    },
    "no_weak_signals": {
        "en": "No weak signals were detected at timestamp {timestamp}.",
        "fr": "Aucun signal faible n'a été détecté à l'horodate {timestamp}.",
        "zh": "在时间戳 {timestamp} 未检测到弱信号。",
    },
    "no_strong_signals": {
        "en": "No strong signals were detected at timestamp {timestamp}.",
        "fr": "Aucun signal fort n'a été détecté à l'horodate {timestamp}.",
        "zh": "在时间戳 {timestamp} 未检测到强信号。",
    },
    "no_noise_signals": {
        "en": "No noisy signals were detected at timestamp {timestamp}.",
        "fr": "Aucun signal de bruit n'a été détecté à l'horodate {timestamp}.",
        "zh": "在时间戳 {timestamp} 未检测到噪声信号。",
    },
    "topic_merging_process": {
        "en": "Topic Merging Process",
        "fr": "Processus de fusion des sujets",
        "zh": "主题合并过程",
    },
    "max_topic_pairs": {
        "en": "Max number of topic pairs to display",
        "fr": "Nombre maximum de paires de sujets à afficher",
        "zh": "要显示的最大主题对数",
    },
    "explore_topic_models": {
        "en": "Explore topic models",
        "fr": "Explorer les modèles de sujets",
        "zh": "探索主题模型",
    },
    "select_model": {
        "en": "Select Model",
        "fr": "Sélectionner le modèle",
        "zh": "选择模型",
    },
    "signal_interpretation": {
        "en": "Signal Interpretation",
        "fr": "Interprétation du signal",
        "zh": "信号解释",
    },
    "analyzing_signal": {
        "en": "Analyzing signal...",
        "fr": "Analyse du signal...",
        "zh": "正在分析信号...",
    },
    "select_date_range": {
        "en": "Select date range for saving signal evolution data:",
        "fr": "Sélectionnez la plage de dates pour l'enregistrement des données d'évolution du signal :",
        "zh": "选择保存信号演变数据的日期范围：",
    },
    "save_signal_evolution_data": {
        "en": "Save Signal Evolution Data",
        "fr": "Enregistrer les données d'évolution du signal",
        "zh": "保存信号演变数据",
    },
    "data_saved_success": {
        "en": "Signal evolution data saved successfully at {path}",
        "fr": "Données d'évolution du signal enregistrées avec succès à {path}",
        "zh": "信号演变数据已成功保存到 {path}",
    },
    "data_saved_error": {
        "en": "Error encountered while saving signal evolution data: {error}",
        "fr": "Erreur rencontrée lors de l'enregistrement des données d'évolution du signal : {error}",
        "zh": "保存信号演变数据时遇到错误：{error}",
    },
    "topic_counts_saved": {
        "en": "Topic counts for individual and cumulative merged models saved to {path}",
        "fr": "Nombre de sujets pour les modèles individuels et fusionnés cumulatifs enregistrés dans {path}",
        "zh": "单个和累积合并模型的主题计数已保存到 {path}",
    },
}