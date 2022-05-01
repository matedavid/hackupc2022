import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    container: {
        height: 100,
        
        backgroundColor: "#e0dede",
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
    },
    bot1: {
        borderRadius: 25,
        marginHorizontal: 20,
        backgroundColor: '#167a27',
        flexDirection: 'row',
    },
    bot2: {
        borderRadius: 25,
        backgroundColor: '#e0240b',
        flexDirection: 'row',
    },
    bot3: {
         borderRadius: 25,
        marginHorizontal: 20,
        backgroundColor: '#e37a09',
        flexDirection: 'row',
    }
});

export default styles;