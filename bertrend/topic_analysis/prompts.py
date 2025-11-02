#  Copyright (c) 2024, RTE (https://www.rte-france.com)
#  See AUTHORS.txt
#  SPDX-License-Identifier: MPL-2.0
#  This file is part of BERTrend.

TOPIC_DESCRIPTION_PROMPT_EN = """
You are a topic analysis expert. Your task is to generate a clear, human-readable title and a detailed description for the given topic.

Input:
- Topic representation: {topic_representation}
- Context documents (may include excerpts, keywords, or summaries):
{docs_text}

Requirements:
1) Title:
   - Be concise (max 8 words)
   - Be informative and specific
   - Use Title Case
   - Avoid jargon and buzzwords unless present in the context

2) Description:
   - ~100 words (90–120 words)
   - Summarize the central idea and scope
   - Highlight key themes, entities, or recurring concepts from the context
   - Avoid copying long verbatim text from the context; paraphrase instead
   - Be neutral, factual, and free of speculation
   - Do not begin with generic phrases such as "This theme...", "This topic...", or "The theme...", or "The topic..."

3) Style & Quality:
   - No placeholders, no extraneous commentary
   - No first-person voice
   - No references to the prompt or instructions
   - Start directly with substantive content (e.g., a key concept, scope, or claim), not with meta-introductions

Output format (strict JSON; no prose outside JSON):
"title": "Your title here",  
"description": "Your ~100-word description here."
"""

TOPIC_DESCRIPTION_PROMPT_FR = """
Vous êtes un expert en analyse de sujets. Votre tâche est de générer un titre clair et lisible ainsi qu’une description détaillée pour le sujet fourni.

Entrée :
- Représentation du sujet : {topic_representation}
- Contexte (extraits, mots-clés ou résumés) :
{docs_text}

Exigences :
1) Titre :
   - Concis (max. 8 mots)
   - Informatif et spécifique
   - Éviter le jargon sauf s’il apparaît dans le contexte

2) Description :
   - Environ 100 mots (90–120)
   - Résumer l’idée centrale et le périmètre
   - Mettre en avant les thèmes, entités ou concepts récurrents du contexte
   - Ne pas copier de longs passages ; reformuler
   - Ton neutre, factuel, sans spéculation
   - Ne pas commencer par des formules génériques telles que « Ce thème… », « Ce sujet… » ou « Le thème… » ou « Le sujet… »

3) Style & Qualité :
   - Pas d’espaces réservés, pas de commentaires superflus
   - Pas de première personne
   - Aucune référence aux instructions
   - Commencer directement par le contenu substantiel (concept clé, périmètre, ou idée centrale), sans méta-introduction

Format de sortie (JSON strict ; aucun texte hors du JSON) :
"title": "Votre titre ici",  
"description": "Votre description (~100 mots) ici."
"""

TOPIC_DESCRIPTION_PROMPT_ZH = """
您是主题分析专家。您的任务是为给定的主题生成清晰、易于理解的标题和详细描述。

输入：
- 主题表示：{topic_representation}
- 上下文文档（可能包含摘录、关键词或摘要）：
{docs_text}

要求：
1) 标题：
   - 简洁（最多8个词）
   - 信息丰富且具体
   - 使用标题大小写
   - 避免使用行话和流行语，除非上下文中出现

2) 描述：
   - 约100字（90-120字）
   - 总结核心思想和范围
   - 突出显示上下文中的关键主题、实体或重复出现的概念
   - 避免从上下文中复制长段文字；应进行转述
   - 保持中立、客观，避免推测
   - 不要以通用短语开头，如"这个主题..."、"这个话题..."或"该主题..."、"该话题..."

3) 风格与质量：
   - 不要使用占位符，不要有额外评论
   - 不要使用第一人称
   - 不要提及提示或指令
   - 直接以实质性内容开头（例如关键概念、范围或主张），不要使用元介绍

输出格式（严格的JSON格式；JSON外不要有其他文本）：
"title": "您的标题在这里",
"description": "您的约100字描述在这里。"
"""

TOPIC_DESCRIPTION_PROMPT = {
    "en": TOPIC_DESCRIPTION_PROMPT_EN,
    "fr": TOPIC_DESCRIPTION_PROMPT_FR,
    "zh": TOPIC_DESCRIPTION_PROMPT_ZH,
}