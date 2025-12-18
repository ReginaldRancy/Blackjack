#!/usr/bin/env bash

set -e

echo "📁 Initialisation de la structure backend..."

# Fichiers racine
touch Dockerfile requirements.txt pytest.ini

# Dossiers principaux
mkdir -p src tests

# ---------- src ----------
touch src/main.py
touch src/__init__.py

# core
mkdir -p src/core
touch src/core/{config.py,database.py,economy.py,randomness.py}

# ---------- domain ----------
mkdir -p src/domain/{agents,accounts,games,perks}

# agents
touch src/domain/agents/{base.py,player.py,bot.py,house.py}

# accounts
touch src/domain/accounts/{wallet.py,portfolio.py}

# games
mkdir -p src/domain/games/{blackjack,stock_market}
touch src/domain/games/base.py

# blackjack
touch src/domain/games/blackjack/{engine.py,rules.py,entities.py}

# stock market
touch src/domain/games/stock_market/{engine.py,market.py,strategies.py}

# perks
touch src/domain/perks/{base.py,luck_boost.py}

# ---------- persistence ----------
mkdir -p src/persistence/{models,repositories}
touch src/persistence/models/{agent.py,account.py,game_state.py}
touch src/persistence/repositories/{agent_repo.py,game_repo.py}

# ---------- api ----------
mkdir -p src/api/v1
touch src/api/v1/{api_router.py,blackjack.py,economy.py}

# ---------- tests ----------
mkdir -p tests/{domain,api}
touch tests/domain/{test_blackjack_engine.py,test_market_simulation.py}

echo "✅ Structure backend créée avec succès."
