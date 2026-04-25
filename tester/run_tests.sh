#!/bin/bash

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# --- Header ---
show_header() {
    clear
    echo -e "${CYAN}==============================================================${NC}"
    echo -e "${BOLD}                MINISHELL INTERACTIVE TESTER                ${NC}"
    echo -e "${CYAN}==============================================================${NC}"
}

# --- Menu ---
show_menu() {
    echo -e "\n${YELLOW}${BOLD}Available Tests:${NC}"
    
    echo -e "\n ${BLUE}--- Run Interactive Sessions ---${NC}"
    echo -e "  ${GREEN}1)${NC} Mandatory tests with ${BOLD}Bash${NC}"
    echo -e "  ${GREEN}2)${NC} Mandatory tests with ${BOLD}Minishell${NC}"
    echo -e "  ${GREEN}3)${NC} Bonus tests with ${BOLD}Bash${NC}"
    echo -e "  ${GREEN}4)${NC} Bonus tests with ${BOLD}Minishell${NC}"
    
    echo -e "\n ${BLUE}--- Comparisons & Reports ---${NC}"
    echo -e "  ${GREEN}5)${NC} Compare ${BOLD}Mandatory${NC} results (Text + MD)"
    echo -e "  ${GREEN}6)${NC} Compare ${BOLD}Bonus${NC} results (Text + MD)"
    
    echo -e "\n ${BLUE}--- Other Tests ---${NC}"
    echo -e "  ${GREEN}7)${NC} Run ${BOLD}Non-Interactive${NC} tests"
    echo -e "  ${GREEN}8)${NC} Test ${BOLD}Exit Codes & Signals${NC} (Ctrl+C, Ctrl+\, Ctrl+D)"

    echo -e "\n ${BLUE}--- Automated Suites ---${NC}"
    echo -e "  ${GREEN}9)${NC} ${BOLD}Run ALL Mandatory${NC} (Interactive, Non-Interactive, Signals)"
    echo -e "  ${GREEN}10)${NC} ${BOLD}Run ALL Bonus${NC} (Interactive, Non-Interactive, Signals)"
    
    echo -e "\n  ${RED}q)${NC} Exit"
    echo -e "${CYAN}--------------------------------------------------------------${NC}"
}

# --- Main Loop ---
while true; do
    show_header
    show_menu
    
    read -p "$(echo -e "${BOLD}Select an option: ${NC}")" choice

    echo -e "\n${CYAN}Executing...${NC}\n"

    case $choice in
        1) expect utils/tester.exp mandatory bash ;;
        2) expect utils/tester.exp mandatory minishell ;;
        3) expect utils/tester.exp bonus bash ;;
        4) expect utils/tester.exp bonus minishell ;;
        5) python3 utils/compare_interactive_results.py interactive mandatory ;;
        6) python3 utils/compare_interactive_results.py interactive bonus ;;
        7) python3 utils/run_noninteractive_tests.py ;;
        8) bash utils/test_exit_codes_signals.sh ;;
        9) 
            echo -e "${YELLOW}Step 1: Running Interactive Mandatory (Bash)${NC}"
            expect utils/tester.exp mandatory bash
            echo -e "${YELLOW}Step 2: Running Interactive Mandatory (Minishell)${NC}"
            expect utils/tester.exp mandatory minishell
            echo -e "${YELLOW}Step 3: Comparing Interactive Results${NC}"
            python3 utils/compare_interactive_results.py interactive mandatory
            echo -e "${YELLOW}Step 4: Running Non-Interactive Mandatory Tests${NC}"
            EXCLUDE="bonus" python3 utils/run_noninteractive_tests.py
            echo -e "${YELLOW}Step 5: Testing Signals & Exit Codes${NC}"
            bash utils/test_exit_codes_signals.sh
            echo -e "${YELLOW}Step 6: Combining Reports${NC}"
            python3 utils/combine_md_reports.py mandatory
            ;;
        10) 
            echo -e "${YELLOW}Step 1: Running Interactive Bonus (Bash)${NC}"
            expect utils/tester.exp bonus bash
            echo -e "${YELLOW}Step 2: Running Interactive Bonus (Minishell)${NC}"
            expect utils/tester.exp bonus minishell
            echo -e "${YELLOW}Step 3: Comparing Interactive Results${NC}"
            python3 utils/compare_interactive_results.py interactive bonus
            echo -e "${YELLOW}Step 4: Running ALL Non-Interactive Tests${NC}"
            python3 utils/run_noninteractive_tests.py
            echo -e "${YELLOW}Step 5: Testing Signals & Exit Codes${NC}"
            bash utils/test_exit_codes_signals.sh
            echo -e "${YELLOW}Step 6: Combining Reports${NC}"
            python3 utils/combine_md_reports.py bonus
            ;;
        q|Q) 
            echo -e "${GREEN}Exiting. Happy coding!${NC}"
            exit 0 
            ;;
        *) 
            echo -e "${RED}Invalid option. Please try again.${NC}" 
            sleep 1
            continue
            ;;
    esac

    echo -e "\n${YELLOW}Execution finished.${NC}"
    read -p "Press enter to return to menu..."
done
