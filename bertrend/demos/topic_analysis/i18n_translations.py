#  Copyright (c) 2024, RTE (https://www.rte-france.com)
#  See AUTHORS.txt
#  SPDX-License-Identifier: MPL-2.0
#  This file is part of BERTrend.

# Translation dictionaries for topic_analysis demo
TRANSLATIONS = {
    "app_title": {
        "fr": "BERTrend - Démo d'analyse de sujets",
        "en": "BERTrend - Topic Analysis demo",
        "zh": "BERTrend - 主题分析演示"
    },
    "data_distribution": {
        "fr": "Distribution des données",
        "en": "Data distribution",
        "zh": "数据分布"
    },
    "time_aggregation": {
        "fr": "Agrégation temporelle",
        "en": "Time aggregation",
        "zh": "时间聚合"
    },
    "save_model": {
        "fr": "Sauvegarder le modèle",
        "en": "Save Model",
        "zh": "保存模型"
    },
    "enter_model_name": {
        "fr": "Entrez un nom pour le modèle (optionnel) :",
        "en": "Enter a name for the model (optional):",
        "zh": "输入模型名称（可选）："
    },
    "model_saved_successfully": {
        "fr": "Modèle sauvegardé avec succès sous {model_save_path}",
        "en": "Model saved successfully as {model_save_path}",
        "zh": "模型已成功保存为 {model_save_path}"
    },
    "training_model": {
        "fr": "Entraînement du modèle...",
        "en": "Training model...",
        "zh": "训练模型中..."
    },
    "train_model": {
        "fr": "Entraîner le modèle",
        "en": "Train Model",
        "zh": "训练模型"
    },
    "review_settings_help": {
        "fr": "Assurez-vous de vérifier les paramètres avant de cliquer sur ce bouton.",
        "en": "Make sure to review the settings before clicking on this button.",
        "zh": "点击此按钮前请确保检查设置。"
    },
    "error_embedding_documents": {
        "fr": "Une erreur s'est produite lors de la vectorisation des documents : {e}",
        "en": "An error occurred while embedding documents: {e}",
        "zh": "嵌入文档时发生错误：{e}"
    },
    "topic_analysis_demo_title": {
        "fr": ":part_alternation_mark: Démo d'analyse de sujets",
        "en": ":part_alternation_mark: Topic analysis demo",
        "zh": ":part_alternation_mark: 主题分析演示"
    },
    "data_loading_training": {
        "fr": "Chargement des données & entraînement du modèle",
        "en": "Data loading & model training",
        "zh": "数据加载和模型训练"
    },
    "topic_exploration": {
        "fr": "Exploration des sujets",
        "en": "Topic exploration",
        "zh": "主题探索"
    },
    "topic_visualization": {
        "fr": "Visualisation des sujets",
        "en": "Topic visualization",
        "zh": "主题可视化"
    },
    "temporal_visualization": {
        "fr": "Visualisation temporelle",
        "en": "Temporal visualization",
        "zh": "时间可视化"
    },
    "newsletter_generation": {
        "fr": "Génération de newsletter",
        "en": "Newsletter generation",
        "zh": "新闻简报生成"
    },
    "topic_analysis": {
        "fr": "Analyse de sujets",
        "en": "Topic Analysis",
        "zh": "主题分析"
    },
    "application_example": {
        "fr": "Exemple d'application",
        "en": "Application example",
        "zh": "应用示例"
    },
    "embeddings_cache_info": {
        "fr": "Les embeddings ne sont pas sauvegardés dans le cache et ne sont donc pas chargés. Veuillez vous assurer d'entraîner le modèle sans utiliser les embeddings en cache si vous souhaitez des visualisations temporelles correctes et fonctionnelles.",
        "en": "Embeddings aren't saved in cache and thus aren't loaded. Please make sure to train the model without using cached embeddings if you want correct and functional temporal visualizations.",
        "zh": "嵌入未保存在缓存中，因此未加载。如果您想要正确且功能正常的时间可视化，请确保在不使用缓存嵌入的情况下训练模型。"
    },
    "save_model_reminder": {
        "fr": "N'oubliez pas de sauvegarder votre modèle !",
        "en": "Don't forget to save your model!",
        "zh": "不要忘记保存您的模型！"
    },
    "no_model_available_error": {
        "fr": "Aucun modèle disponible à sauvegarder. Veuillez d'abord entraîner un modèle.",
        "en": "No model available to save. Please train a model first.",
        "zh": "没有可保存的模型。请先训练模型。"
    },
    "no_document_for_topic": {
        "fr": "Aucun document trouvé pour le sujet sélectionné.",
        "en": "No documents found for the selected topic.",
        "zh": "未找到所选主题的文档。"
    },
    "train_model_first_error": {
        "fr": "Veuillez d'abord entraîner un modèle.",
        "en": "Please train a model first.",
        "zh": "请先训练模型。"
    },
    "remote_embedding_service_type_not_supported_error": {
        "fr": "Ces visualisations ne sont disponibles que si un service d'embedding local est utilisé.",
        "en": "These visualizations are only available if a local embedding service is used.",
        "zh": "仅在使用本地嵌入服务时才能使用这些可视化。"
    },
    "visualizations": {
        "fr": "Visualisations",
        "en": "Visualizations",
        "zh": "可视化"
    },
    "include_outliers": {
        "en": "Include outliers (Topic = -1)",
        "fr": "Inclure les outliers (Topic = -1)",
        "zh": "包含离群值（主题 = -1）"
    },
    "overall_results": {
        "en": "Overall results",
        "fr": "Aperçu des résultats",
        "zh": "总体结果"
    },
    "overall_results_display_error": {
        "en": "Cannot display overall results",
        "fr": "Impossible d'afficher l'aperçu des résultats",
        "zh": "无法显示总体结果"
    },
    "change_umap_params_warning": {
        "en": "Try to change the UMAP parameters",
        "fr": "Essayez de changer les paramètres UMAP",
        "zh": "尝试更改 UMAP 参数"
    },
    "topics_treemap": {"en": "Topics Treemap", "fr": "Topics Treemap", "zh": "主题树状图"},
    "topics_treemap_computation": {
        "en": "Computing topics treemap...",
        "fr": "Calcul du treemap des sujets...",
        "zh": "计算主题树状图中..."
    },
    "data_map": {"en": "Data Map", "fr": "Carte des données", "zh": "数据地图"},
    "data_map_loading": {
        "en": "Loading Data-map plot...",
        "fr": "Chargement de la carte des données...",
        "zh": "加载数据地图中..."
    },
    "full_screen": {"en": "Full screen", "fr": "Affichage plein écran", "zh": "全屏显示"},
    "no_data_map_warning": {
        "en": "No valid topics to visualize. All documents might be classified as outliers.",
        "fr": "Pas de sujets à visualiser. Peut-être trop d'outliers.",
        "zh": "没有有效的主题可可视化。所有文档可能被分类为离群值。"
    },
    # TEMPTopic Parameters section
    "temptopic_parameters": {
        "en": "TEMPTopic Parameters",
        "fr": "Paramètres TEMPTopic",
        "zh": "TEMPTopic 参数"
    },
    "window_size": {"en": "Window Size", "fr": "Taille de fenêtre", "zh": "窗口大小"},
    "k_nearest_embeddings": {
        "en": "Number of Nearest Embeddings (k)",
        "fr": "Nombre d'Embeddings les plus proches (k)",
        "zh": "最近嵌入数量 (k)"
    },
    "k_nearest_help": {
        "en": "The k-th nearest neighbor used for Topic Representation Stability calculation.",
        "fr": "Le k-ième voisin le plus proche utilisé pour le calcul de la stabilité de représentation des sujets.",
        "zh": "用于主题表示稳定性计算的第 k 个最近邻。"
    },
    "alpha_weight": {
        "en": "Alpha (Topic vs Representation Stability Weight)",
        "fr": "Alpha (Poids de Stabilité du Sujet vs Représentation)",
        "zh": "Alpha（主题与表示稳定性权重）"
    },
    "alpha_help": {
        "en": "Closer to 1 gives more weight given to Topic Embedding Stability, Closer to 0 gives more weight to topic representation stability.",
        "fr": "Plus proche de 1 donne plus de poids à la stabilité de l'embedding du sujet, plus proche de 0 donne plus de poids à la stabilité de la représentation du sujet.",
        "zh": "接近 1 则更重视主题嵌入稳定性，接近 0 则更重视主题表示稳定性。"
    },
    "use_double_agg": {
        "en": "Use Double Aggregation",
        "fr": "Utiliser l'Agrégation Double",
        "zh": "使用双重聚合"
    },
    "double_agg_help": {
        "en": "If unchecked, only Document Aggregation Method will be globally used.",
        "fr": "Si non coché, seule la méthode d'agrégation de documents sera utilisée globalement.",
        "zh": "如果未选中，则全局仅使用文档聚合方法。"
    },
    "doc_agg_method": {
        "en": "Document Aggregation Method",
        "fr": "Méthode d'Agrégation de Documents",
        "zh": "文档聚合方法"
    },
    "global_agg_method": {
        "en": "Global Aggregation Method",
        "fr": "Méthode d'Agrégation Globale",
        "zh": "全局聚合方法"
    },
    "use_evolution_tuning": {
        "en": "Use Evolution Tuning",
        "fr": "Utiliser Evolution Tuning",
        "zh": "使用进化调优"
    },
    "use_global_tuning": {
        "en": "Use Global Tuning",
        "fr": "Utiliser Global Tuning",
        "zh": "使用全局调优"
    },
    # Time granularity section
    "select_time_granularity": {
        "en": "Select custom time granularity",
        "fr": "Sélectionner la granularité temporelle personnalisée",
        "zh": "选择自定义时间粒度"
    },
    "days": {"en": "Days", "fr": "Jours", "zh": "天"},
    "hours": {"en": "Hours", "fr": "Heures", "zh": "小时"},
    "minutes": {"en": "Minutes", "fr": "Minutes", "zh": "分钟"},
    "seconds": {"en": "Seconds", "fr": "Secondes", "zh": "秒"},
    "granularity_info": {
        "en": "Granularity must be greater than zero and less than or equal to {max_granularity}.",
        "fr": "La granularité doit être supérieure à zéro et inférieure ou égale à {max_granularity}.",
        "zh": "粒度必须大于零且小于等于 {max_granularity}。"
    },
    # Buttons and controls
    "apply_granularity": {
        "en": "Apply Granularity and Parameters",
        "fr": "Appliquer la Granularité et les Paramètres",
        "zh": "应用粒度和参数"
    },
    "show_table_results": {
        "en": "Show table results",
        "fr": "Afficher les résultats du tableau",
        "zh": "显示表格结果"
    },
    "topic_evolution": {"en": "Topic evolution", "fr": "Évolution des sujets", "zh": "主题演变"},
    "topic_info": {"en": "Topic info", "fr": "Informations sur les sujets", "zh": "主题信息"},
    "documents_per_date": {"en": "Documents per date", "fr": "Documents par date", "zh": "每日文档数"},
    # Dataframes and expandable sections
    "topic_evolution_dataframe": {
        "en": "Topic Evolution Dataframe",
        "fr": "Dataframe d'évolution des sujets",
        "zh": "主题演变数据框"
    },
    "topic_info_dataframe": {
        "en": "Topic Info Dataframe",
        "fr": "Dataframe d'informations sur les sujets",
        "zh": "主题信息数据框"
    },
    "documents_per_date_dataframe": {
        "en": "Documents per Date Dataframe",
        "fr": "Dataframe des documents par date",
        "zh": "每日文档数据框"
    },
    "temptopic_visualizations": {
        "en": "TempTopic Visualizations",
        "fr": "Visualisations TempTopic",
        "zh": "TempTopic 可视化"
    },
    # Visualization settings
    "topics_to_show": {"en": "Topics to Show", "fr": "Sujets à Afficher", "zh": "要显示的主题"},
    "topic_evolution_header": {
        "en": "Topic Evolution in Time and Semantic Space",
        "fr": "Évolution des Sujets dans le temps et l'espace sémantique",
        "zh": "时间和语义空间中的主题演变"
    },
    "umap_n_neighbors": {"en": "UMAP n_neighbors", "fr": "UMAP n_neighbors", "zh": "UMAP n_neighbors"},
    "umap_min_dist": {"en": "UMAP min_dist", "fr": "UMAP min_dist", "zh": "UMAP min_dist"},
    "umap_metric": {"en": "UMAP Metric", "fr": "UMAP Metric", "zh": "UMAP 度量"},
    "color_palette": {"en": "Color Palette", "fr": "Palette de Couleurs", "zh": "调色板"},
    "overall_topic_stability": {
        "en": "Overall Topic Stability",
        "fr": "Stabilité globale des sujets",
        "zh": "整体主题稳定性"
    },
    "normalize": {"en": "Normalize", "fr": "Normaliser", "zh": "归一化"},
    "temporal_stability_metrics": {
        "en": "Temporal Stability Metrics",
        "fr": "Métriques de stabilité temporelle",
        "zh": "时间稳定性指标"
    },
    # Topic popularity
    "popularity_of_topics": {
        "en": "Popularity of topics over time",
        "fr": "Popularité des sujets au fil du temps",
        "zh": "主题随时间的热度"
    },
    "topics_list_format": {
        "en": "Topics list (format 1,12,52 or 1:20)",
        "fr": "Liste des sujets (format 1,12,52 ou 1:20)",
        "zh": "主题列表（格式 1,12,52 或 1:20）"
    },
    "nr_bins": {"en": "nr_bins", "fr": "nombre_de_bins", "zh": "分箱数"},
    # Messages
    "apply_granularity_message": {
        "en": "Please apply granularity and parameters to view the temporal visualizations.",
        "fr": "Veuillez appliquer la granularité et les paramètres pour voir les visualisations temporelles.",
        "zh": "请应用粒度和参数以查看时间可视化。"
    },
    "fitting_temptopic": {
        "en": "Fitting TempTopic...",
        "fr": "Fitting de TempTopic...",
        "zh": "拟合 TempTopic 中..."
    },
    "computing_topics": {
        "en": "Computing topics over time...",
        "fr": "Calcul des sujets au fil du temps...",
        "zh": "计算随时间变化的主题中..."
    },
    "select_valid_granularity": {
        "en": "Please select a valid granularity before applying.",
        "fr": "Veuillez sélectionner une granularité valide avant d'appliquer.",
        "zh": "应用前请选择有效的粒度。"
    },
    "temporal_visualizations": {
        "en": "Temporal visualizations of topics",
        "fr": "Visualisations temporelles des sujets",
        "zh": "主题的时间可视化"
    },
    # New translations for newsletter functionality
    "newsletter_generation_title": {
        "en": "Automatic newsletters generation",
        "fr": "Génération automatique de newsletters",
        "zh": "自动新闻简报生成"
    },
    "include_all_topics": {"en": "Include all topics", "fr": "Inclure tous les sujets", "zh": "包含所有主题"},
    "number_of_topics": {"en": "Number of topics", "fr": "Nombre de sujets", "zh": "主题数量"},
    "include_all_documents": {
        "en": "Include all documents per topic",
        "fr": "Inclure tous les documents par sujet",
        "zh": "每个主题包含所有文档"
    },
    "number_of_docs_per_topic": {
        "en": "Number of docs per topic",
        "fr": "Nombre de documents par sujet",
        "zh": "每个主题的文档数"
    },
    "improve_topic_description": {
        "en": "Improve topic description",
        "fr": "Améliorer la description du sujet",
        "zh": "改进主题描述"
    },
    "summary_mode": {"en": "Summary mode", "fr": "Mode de résumé", "zh": "摘要模式"},
    "summarizer_class": {
        "en": "Summarizer class",
        "fr": "Classe utilisée pour le résumé",
        "zh": "摘要器类"
    },
    "generate_newsletter_button": {
        "en": "Generate newsletter",
        "fr": "Générer la newsletter",
        "zh": "生成新闻简报"
    },
    "generating_newsletters": {
        "en": "Generating newsletters...",
        "fr": "Génération des newsletters...",
        "zh": "生成新闻简报中..."
    },
    # New translations for topic exploration functionality
    "topics_exploration": {"en": "Topics exploration", "fr": "Exploration des sujets", "zh": "主题探索"},
    "search_topic": {"en": "Search topic", "fr": "Rechercher un sujet", "zh": "搜索主题"},
    "topic": {"en": "Topic", "fr": "Sujet", "zh": "主题"},
    "documents_lowercase": {"en": "documents", "fr": "documents", "zh": "文档"},
    "unknown_source": {"en": "Unknown Source", "fr": "Source Inconnue", "zh": "未知来源"},
    "new_documents": {"en": "New documents", "fr": "Nouveaux documents", "zh": "新文档"},
    "generate_topic_description": {
        "en": "Generate a short description of the topic",
        "fr": "Générer une description courte du sujet",
        "zh": "生成主题的简短描述"
    },
    "generating_description": {
        "en": "Generating the description...",
        "fr": "Génération de la description en cours...",
        "zh": "生成描述中..."
    },
    "number_of_articles_to_display": {
        "en": "Number of articles to display",
        "fr": "Nombre d'articles à afficher",
        "zh": "要显示的文章数量"
    },
    "select_sources_to_display": {
        "en": "Select the sources to display",
        "fr": "Sélectionner les sources à afficher",
        "zh": "选择要显示的来源"
    },
    "all": {"en": "All", "fr": "Toutes", "zh": "全部"},
    "export_configuration": {
        "en": "Export Configuration",
        "fr": "Configuration de l'export",
        "zh": "导出配置"
    },
    "choose_export_method": {
        "en": "Choose export method:",
        "fr": "Choisir la méthode d'export :",
        "zh": "选择导出方法："
    },
    "download_as_zip": {"en": "Download as ZIP", "fr": "Télécharger en ZIP", "zh": "下载为 ZIP"},
    "save_to_folder": {"en": "Save to folder", "fr": "Enregistrer dans un dossier", "zh": "保存到文件夹"},
    "export_method_help": {
        "en": "Select whether to download documents as a ZIP file or save them directly to a folder on the server.",
        "fr": "Sélectionnez si vous souhaitez télécharger les documents sous forme de fichier ZIP ou les enregistrer directement dans un dossier sur le serveur.",
        "zh": "选择是将文档下载为 ZIP 文件还是直接保存到服务器上的文件夹中。"
    },
    "granularity_days": {
        "en": "Granularity (number of days)",
        "fr": "Granularité (nombre de jours)",
        "zh": "粒度（天数）"
    },
    "export_topic_documents": {
        "en": "Export Topic Documents",
        "fr": "Exporter les Documents associés au Sujet",
        "zh": "导出主题文档"
    },
    "export_success": {
        "en": "Successfully exported documents to folder: {export_folder}",
        "fr": "Documents exportés avec succès dans le dossier : {export_folder}",
        "zh": "成功将文档导出到文件夹：{export_folder}"
    },
}