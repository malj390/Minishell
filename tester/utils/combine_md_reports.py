#!/usr/bin/env python3
import os
import sys

def combine_reports(test_type):
    """
    test_type: 'mandatory' or 'bonus'
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(base_dir, 'results')
    
    output_file = os.path.join(base_dir, f'{test_type.capitalize()}_tests.md')
    
    # Files to combine
    files = [
        os.path.join(results_dir, f'comparison_interactive_{test_type}.md'),
        os.path.join(results_dir, 'noninteractive_comparison.md'),
        os.path.join(results_dir, 'signals_comparison.md')
    ]
    
    titles = [
        "## Interactive Tests",
        "## Non-Interactive Tests",
        "## Signal and Exit Code Tests"
    ]
    
    with open(output_file, 'w') as out:
        out.write(f"# Minishell {test_type.capitalize()} Test Suite Report\n\n")
        
        for i, file_path in enumerate(files):
            out.write(f"{titles[i]}\n\n")
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Skip the first header line if it starts with #
                    lines = content.splitlines()
                    start_idx = 0
                    if lines and lines[0].startswith('#'):
                        start_idx = 1
                    out.write('\n'.join(lines[start_idx:]))
            else:
                out.write(f"*Report not found: {os.path.basename(file_path)}*\n")
            
            out.write("\n\n---\n\n")
            
    print(f"Combined report generated: {output_file}")

if __name__ == "__main__":
    t_type = sys.argv[1] if len(sys.argv) > 1 else "mandatory"
    combine_reports(t_type)
